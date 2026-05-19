# Decision Report

- generated_at: 2026-05-19T20:58:41.340877+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4498**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4498, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=-1.55%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.55% | **-1.55%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 10/20 | 50.0% | +2.54% | **+1.27%** |
| LIMIT_8PCT | 5/20 | 25.0% | +2.34% | **+0.59%** |
| LIMIT_BB3S | 6/11 | 54.5% | +1.05% | **+0.57%** |
| LIMIT_5PCT | 11/20 | 55.0% | +0.88% | **+0.49%** |
| LIMIT_7PCT | 6/20 | 30.0% | +1.40% | **+0.42%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 5/9 | 55.6% | +3.39% | **+1.88%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +3.39% | **+1.87%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +1.89% | **+1.51%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +3.01% | **+1.51%** |
| LIMIT_2PCT_LONG | 11/20 | 55.0% | +2.12% | **+1.16%** |

## 2. $100 Live Portfolio

- 残高: **$96.21** / 初期 $100.00 (-3.79%)
- 確定トレード: 55件 (TP 14 / SL 38 / EXP 3)
- 最新: EDEN/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.21
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定: 473件 (Win 124 / Loss 164 / Flat 185) / skip 586件
- 成長率目線: 平均log +0.000412 / 幾何平均 +0.041% per trade / maxDD +4.21%
- 次の候補: `LIMIT_6PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $121.49

## 4. Latest Market Context

- 更新: 2026-05-19T20:58:39.109606+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.27% price=76986.4
- Funnel: target 760 → liquid 139 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 80.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PROMPT/USDT:USDT | +30.04% | $1,104,311.85 |
| EDEN/USDT:USDT | +22.36% | $13,646,560.36 |
| VVV/USDT:USDT | +13.92% | $11,217,463.84 |
| BANANAS31/USDT:USDT | +12.92% | $1,117,502.22 |
| LIT/USDT:USDT | +11.10% | $2,395,865.22 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BANANAS31/USDT:USDT | below_1h_threshold | +4.84% | +4.57% |
| GUA/USDT:USDT | below_1h_threshold | +3.08% | +2.81% |
| HOME/USDT:USDT | below_1h_threshold | +3.00% | +2.73% |
| CFX/USDT:USDT | below_1h_threshold | +2.03% | +1.77% |
| LIT/USDT:USDT | below_1h_threshold | +1.69% | +1.42% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
