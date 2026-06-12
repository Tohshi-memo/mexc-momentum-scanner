# Decision Report

- generated_at: 2026-06-12T07:40:43.529491+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6481**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6481, expectancy=-0.07%
- 直近20件 MARKET基準: n=20, expectancy=-2.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.20% | **-2.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 3/20 | 15.0% | +3.20% | **+0.48%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.95% | **+0.29%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +0.03% | **+0.01%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +2.20% | **+2.20%** |
| ASK_LONG | 20/20 | 100.0% | +1.97% | **+1.97%** |
| LIMIT_ATR_LONG | 7/20 | 35.0% | +4.36% | **+1.53%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +2.03% | **+1.42%** |
| LIMIT_FIB1272_LONG | 4/20 | 20.0% | +5.98% | **+1.20%** |

## 2. $100 Live Portfolio

- 残高: **$95.17** / 初期 $100.00 (-4.83%)
- 確定トレード: 17件 (TP 2 / SL 14 / EXP 1)
- 最新: ZBT/USDT:USDT SL_HIT PnL -4.00% 残高後 $95.17
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$163.96** / 初期 $100.00 (+63.96%)
- 確定: 1356件 (Win 366 / Loss 434 / Flat 556) / skip 1686件
- 成長率目線: 平均log +0.000365 / 幾何平均 +0.036% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HMSTR/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $163.96

## 4. Latest Market Context

- 更新: 2026-06-12T07:40:40.017729+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.16% price=63055.0
- Funnel: target 779 → liquid 156 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=1, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 71.1 >= 65=1, 4h RSI 67.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VELVET/USDT:USDT | +104.44% | $141,493,466.97 |
| NAORIS/USDT:USDT | +39.88% | $2,258,441.98 |
| ESPORTS/USDT:USDT | +36.67% | $35,100,577.39 |
| H/USDT:USDT | +36.04% | $44,503,604.63 |
| XPL/USDT:USDT | +34.60% | $7,554,261.02 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NAORIS/USDT:USDT | below_relative_strength | +5.10% | +4.94% |
| VELVET/USDT:USDT | below_1h_threshold | +3.92% | +3.76% |
| H/USDT:USDT | below_1h_threshold | +3.78% | +3.62% |
| LAB/USDT:USDT | below_1h_threshold | +3.66% | +3.50% |
| NEAR/USDT:USDT | below_1h_threshold | +3.03% | +2.87% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
