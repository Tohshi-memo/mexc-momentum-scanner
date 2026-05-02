# Decision Report

- generated_at: 2026-05-02T14:42:51.056569+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2921**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=2921, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=-3.17%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -3.17% | **-3.17%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 5/20 | 25.0% | +6.28% | **+1.57%** |
| LIMIT_6PCT | 10/20 | 50.0% | +2.50% | **+1.25%** |
| LIMIT_9PCT | 3/20 | 15.0% | +8.00% | **+1.20%** |
| LIMIT_7PCT | 6/20 | 30.0% | +3.67% | **+1.10%** |
| LIMIT_5PCT | 12/20 | 60.0% | -0.29% | **-0.17%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +2.59% | **+2.59%** |
| ASK_LONG | 20/20 | 100.0% | +2.30% | **+2.30%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +2.74% | **+2.05%** |
| LIMIT_6PCT_LONG | 4/20 | 20.0% | +5.47% | **+1.09%** |
| LIMIT_5PCT_LONG | 4/20 | 20.0% | +5.21% | **+1.04%** |

## 2. $100 Live Portfolio

- 残高: **$101.99** / 初期 $100.00 (+1.99%)
- 確定トレード: 8件 (TP 4 / SL 4 / EXP 0)
- 最新: NAORIS/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.99
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-02T14:42:48.021514+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.02% price=78346.5
- Funnel: target 755 → liquid 161 → pre 50 → checked 50 → surge 5 → strict 0
- Surge前reject: below_1h_threshold=45, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 95.7 >= 65=1, 4h RSI 90.6 >= 65=1, 4h RSI 82.2 >= 65=1, 4h RSI 67.4 >= 65=1, 4h RSI 71.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LAB/USDT:USDT | +288.12% | $152,890,819.80 |
| TAG/USDT:USDT | +57.50% | $8,649,358.87 |
| BIO/USDT:USDT | +52.86% | $3,403,499.64 |
| B/USDT:USDT | +26.72% | $73,233,842.40 |
| SPACE/USDT:USDT | +26.62% | $1,481,320.52 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TAG/USDT:USDT | below_1h_threshold | +4.88% | +4.86% |
| KNC/USDT:USDT | below_1h_threshold | +4.00% | +3.98% |
| ZBT/USDT:USDT | below_1h_threshold | +3.92% | +3.90% |
| BSB/USDT:USDT | below_1h_threshold | +3.82% | +3.80% |
| XNY/USDT:USDT | below_1h_threshold | +2.49% | +2.48% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
