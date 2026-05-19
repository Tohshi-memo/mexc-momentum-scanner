# Decision Report

- generated_at: 2026-05-19T15:58:42.808205+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4476**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4476, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=+0.16%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.16% | **+0.16%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_5PCT | 5/20 | 25.0% | +0.95% | **+0.24%** |
| MARKET | 20/20 | 100.0% | +0.16% | **+0.16%** |
| ASK | 20/20 | 100.0% | +0.15% | **+0.15%** |
| LIMIT_4PCT | 11/20 | 55.0% | +0.03% | **+0.02%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/5 | 60.0% | +2.76% | **+1.66%** |
| MARKET_LONG | 20/20 | 100.0% | +0.70% | **+0.70%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +3.15% | **+0.63%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +1.97% | **+0.59%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +1.49% | **+0.52%** |

## 2. $100 Live Portfolio

- 残高: **$96.21** / 初期 $100.00 (-3.79%)
- 確定トレード: 55件 (TP 14 / SL 38 / EXP 3)
- 最新: EDEN/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.21
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定: 473件 (Win 124 / Loss 164 / Flat 185) / skip 564件
- 成長率目線: 平均log +0.000412 / 幾何平均 +0.041% per trade / maxDD +4.21%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $121.49

## 4. Latest Market Context

- 更新: 2026-05-19T15:58:40.599784+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.15% price=76480.7
- Funnel: target 764 → liquid 136 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 78.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ZEST/USDT:USDT | +81.35% | $1,038,382.94 |
| PLAY/USDT:USDT | +32.65% | $6,546,802.56 |
| RON/USDT:USDT | +31.47% | $15,114,224.37 |
| EDEN/USDT:USDT | +26.76% | $4,014,139.27 |
| ENJ/USDT:USDT | +14.97% | $1,693,074.94 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| H/USDT:USDT | below_1h_threshold | +3.53% | +3.38% |
| ESPORTS/USDT:USDT | below_1h_threshold | +1.93% | +1.78% |
| KITE/USDT:USDT | below_1h_threshold | +1.79% | +1.64% |
| ZEC/USDT:USDT | below_1h_threshold | +1.73% | +1.58% |
| LIT/USDT:USDT | below_1h_threshold | +1.69% | +1.54% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
