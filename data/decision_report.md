# Decision Report

- generated_at: 2026-06-03T08:33:05.659781+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5535**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5535, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.00% | **+0.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 15/20 | 75.0% | +1.75% | **+1.31%** |
| ASK | 20/20 | 100.0% | +0.77% | **+0.77%** |
| LIMIT_5PCT | 7/20 | 35.0% | +1.96% | **+0.69%** |
| LIMIT_3PCT | 15/20 | 75.0% | +0.67% | **+0.51%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +1.18% | **+0.47%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT_LONG | 12/20 | 60.0% | +0.83% | **+0.50%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +0.67% | **+0.40%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +2.00% | **+0.40%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | -0.03% | **-0.02%** |
| LIMIT_10PCT_LONG | 4/20 | 20.0% | -0.89% | **-0.18%** |

## 2. $100 Live Portfolio

- 残高: **$96.61** / 初期 $100.00 (-3.39%)
- 確定トレード: 90件 (TP 26 / SL 61 / EXP 3)
- 最新: VVV/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.61
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$129.24** / 初期 $100.00 (+29.24%)
- 確定: 989件 (Win 233 / Loss 306 / Flat 450) / skip 1107件
- 成長率目線: 平均log +0.000259 / 幾何平均 +0.026% per trade / maxDD +7.25%
- 次の候補: `LIMIT_6PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PLAY/USDT:USDT `LIMIT_6PCT` SL_HIT account +0.24% 残高後 $129.24

## 4. Latest Market Context

- 更新: 2026-06-03T08:33:00.462561+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.22% price=67039.9
- Funnel: target 771 → liquid 153 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PORTAL/USDT:USDT | +37.86% | $14,564,511.91 |
| CLO/USDT:USDT | +33.01% | $3,511,854.16 |
| GENIUS/USDT:USDT | +30.10% | $1,865,336.71 |
| ENA/USDT:USDT | +24.79% | $49,089,106.95 |
| US/USDT:USDT | +24.58% | $8,693,100.65 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| US/USDT:USDT | below_1h_threshold | +4.63% | +4.85% |
| CLO/USDT:USDT | below_1h_threshold | +4.58% | +4.80% |
| LIT/USDT:USDT | below_1h_threshold | +2.26% | +2.48% |
| ZORA/USDT:USDT | below_1h_threshold | +2.09% | +2.31% |
| BEAT/USDT:USDT | below_1h_threshold | +1.88% | +2.10% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
