# Decision Report

- generated_at: 2026-07-01T00:46:21.990580+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7935**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7935, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=+0.02%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.02% | **+0.02%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 3/20 | 15.0% | +5.96% | **+0.89%** |
| LIMIT_ATR | 15/20 | 75.0% | +0.56% | **+0.42%** |
| LIMIT_5PCT | 6/20 | 30.0% | +1.04% | **+0.31%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +0.43% | **+0.17%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.04% | **+0.03%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +3.56% | **+0.71%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +1.40% | **+0.70%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +2.19% | **+0.22%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +0.25% | **+0.10%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +0.23% | **+0.08%** |

## 2. $100 Live Portfolio

- 残高: **$102.64** / 初期 $100.00 (+2.64%)
- 確定トレード: 47件 (TP 17 / SL 29 / EXP 1)
- 最新: AGLD/USDT:USDT TP_HIT PnL +8.00% 残高後 $102.64
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$256.55** / 初期 $100.00 (+156.55%)
- 確定: 2356件 (Win 714 / Loss 787 / Flat 855) / skip 2140件
- 成長率目線: 平均log +0.000400 / 幾何平均 +0.040% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AIGENSYN/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $256.55

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.52** / 初期 $100.00 (+6.52%)
- 確定: 477件 (Win 125 / Loss 121 / Flat 231) / skip 869件
- 成長率目線: 平均log +0.000132 / 幾何平均 +0.013% per trade / maxDD +3.03%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0314 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BTW/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $106.52

## 5. Latest Market Context

- 更新: 2026-07-01T00:46:13.710180+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.24% price=58459.3
- Funnel: target 818 → liquid 153 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 66.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TAIKO/USDT:USDT | +25.42% | $1,406,655.50 |
| AIGENSYN/USDT:USDT | +15.18% | $14,591,900.76 |
| OPG/USDT:USDT | +12.71% | $1,097,442.66 |
| BESTOCK/USDT:USDT | +12.20% | $1,174,608.95 |
| BASED/USDT:USDT | +10.00% | $2,913,219.50 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| H/USDT:USDT | below_1h_threshold | +3.52% | +3.77% |
| BEAT/USDT:USDT | below_1h_threshold | +3.06% | +3.30% |
| RE/USDT:USDT | below_1h_threshold | +3.02% | +3.27% |
| XLM/USDT:USDT | below_1h_threshold | +2.92% | +3.16% |
| AIGENSYN/USDT:USDT | below_1h_threshold | +2.23% | +2.48% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
