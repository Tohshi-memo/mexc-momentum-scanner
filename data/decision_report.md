# Decision Report

- generated_at: 2026-05-02T15:37:08.435892+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2933**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=2933, expectancy=-0.17%
- 直近20件 MARKET基準: n=20, expectancy=-2.52%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.52% | **-2.52%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 5/20 | 25.0% | +5.92% | **+1.48%** |
| LIMIT_6PCT | 8/20 | 40.0% | +3.42% | **+1.37%** |
| LIMIT_5PCT | 13/20 | 65.0% | +1.66% | **+1.08%** |
| LIMIT_8PCT | 3/20 | 15.0% | +6.57% | **+0.99%** |
| LIMIT_BB3S | 4/16 | 25.0% | +2.39% | **+0.60%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/4 | 75.0% | +6.62% | **+4.97%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +2.21% | **+1.99%** |
| MARKET_LONG | 20/20 | 100.0% | +1.74% | **+1.74%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +2.67% | **+1.34%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +2.00% | **+1.20%** |

## 2. $100 Live Portfolio

- 残高: **$101.99** / 初期 $100.00 (+1.99%)
- 確定トレード: 8件 (TP 4 / SL 4 / EXP 0)
- 最新: NAORIS/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.99
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-02T15:37:05.567024+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.01% price=78376.4
- Funnel: target 755 → liquid 161 → pre 50 → checked 50 → surge 4 → strict 0
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 89.2 >= 65=1, 4h RSI 78.8 >= 65=1, 4h RSI 76.3 >= 65=1, 4h RSI 80.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LAB/USDT:USDT | +306.52% | $167,415,304.07 |
| TAG/USDT:USDT | +69.78% | $10,156,479.55 |
| BIO/USDT:USDT | +43.34% | $3,995,256.47 |
| SKYAI/USDT:USDT | +37.14% | $19,419,272.18 |
| KNC/USDT:USDT | +31.69% | $2,284,882.46 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LAB/USDT:USDT | below_1h_threshold | +3.84% | +3.85% |
| TAG/USDT:USDT | below_1h_threshold | +3.42% | +3.42% |
| B/USDT:USDT | below_1h_threshold | +3.28% | +3.29% |
| UB/USDT:USDT | below_1h_threshold | +1.80% | +1.80% |
| XNY/USDT:USDT | below_1h_threshold | +1.78% | +1.79% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
