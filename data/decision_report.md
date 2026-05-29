# Decision Report

- generated_at: 2026-05-29T05:54:19.502224+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5015**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5015, expectancy=-0.07%
- 直近20件 MARKET基準: n=20, expectancy=-0.56%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.56% | **-0.56%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 7/20 | 35.0% | +3.32% | **+1.16%** |
| LIMIT_8PCT | 5/20 | 25.0% | +3.88% | **+0.97%** |
| LIMIT_6PCT | 7/20 | 35.0% | +1.92% | **+0.67%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | +0.62% | **+0.28%** |
| LIMIT_5PCT | 8/20 | 40.0% | +0.60% | **+0.24%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.20% | **+1.20%** |
| ASK_LONG | 20/20 | 100.0% | +1.10% | **+1.10%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.13% | **+0.96%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +0.90% | **+0.50%** |

## 2. $100 Live Portfolio

- 残高: **$98.61** / 初期 $100.00 (-1.39%)
- 確定トレード: 71件 (TP 21 / SL 47 / EXP 3)
- 最新: BILL/USDT:USDT TP_HIT PnL +8.00% 残高後 $98.61
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$126.95** / 初期 $100.00 (+26.95%)
- 確定: 737件 (Win 175 / Loss 224 / Flat 338) / skip 839件
- 成長率目線: 平均log +0.000324 / 幾何平均 +0.032% per trade / maxDD +4.72%
- 次の候補: `LIMIT_7PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ALLO/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $126.95

## 4. Latest Market Context

- 更新: 2026-05-29T05:54:14.359173+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.25% price=73649.7
- Funnel: target 777 → liquid 149 → pre 50 → checked 50 → surge 4 → strict 3
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 96.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ALLO/USDT:USDT | +119.20% | $40,131,468.00 |
| CTR/USDT:USDT | +39.53% | $1,199,977.21 |
| DELLSTOCK/USDT:USDT | +36.62% | $8,191,029.28 |
| CLO/USDT:USDT | +27.85% | $1,588,449.06 |
| AIGENSYN/USDT:USDT | +19.95% | $1,205,911.38 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NIL/USDT:USDT | below_1h_threshold | +4.88% | +4.63% |
| AIGENSYN/USDT:USDT | below_1h_threshold | +4.70% | +4.45% |
| CLO/USDT:USDT | below_1h_threshold | +4.31% | +4.07% |
| XLM/USDT:USDT | below_1h_threshold | +3.94% | +3.69% |
| INJ/USDT:USDT | below_1h_threshold | +3.27% | +3.02% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
