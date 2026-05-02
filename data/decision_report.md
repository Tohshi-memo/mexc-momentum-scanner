# Decision Report

- generated_at: 2026-05-02T14:22:16.271476+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2915**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=2915, expectancy=-0.15%
- 直近20件 MARKET基準: n=20, expectancy=-2.79%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.79% | **-2.79%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 5/20 | 25.0% | +6.28% | **+1.57%** |
| LIMIT_9PCT | 3/20 | 15.0% | +8.00% | **+1.20%** |
| LIMIT_6PCT | 9/20 | 45.0% | +2.57% | **+1.15%** |
| LIMIT_7PCT | 6/20 | 30.0% | +3.67% | **+1.10%** |
| LIMIT_5PCT | 12/20 | 60.0% | -0.29% | **-0.17%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +2.19% | **+2.19%** |
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +2.00% | **+2.00%** |
| ASK_LONG | 20/20 | 100.0% | +1.81% | **+1.81%** |
| LIMIT_5PCT_LONG | 6/20 | 30.0% | +4.28% | **+1.28%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +1.59% | **+1.12%** |

## 2. $100 Live Portfolio

- 残高: **$101.99** / 初期 $100.00 (+1.99%)
- 確定トレード: 8件 (TP 4 / SL 4 / EXP 0)
- 最新: NAORIS/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.99
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-02T14:22:13.129905+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.05% price=78295.2
- Funnel: target 755 → liquid 160 → pre 50 → checked 50 → surge 4 → strict 0
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 95.6 >= 65=1, 4h RSI 90.7 >= 65=1, 4h RSI 67.8 >= 65=1, 4h RSI 73.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LAB/USDT:USDT | +279.12% | $146,430,569.34 |
| TAG/USDT:USDT | +57.52% | $8,087,068.39 |
| BIO/USDT:USDT | +47.47% | $3,181,587.27 |
| B/USDT:USDT | +27.63% | $72,385,334.01 |
| SKYAI/USDT:USDT | +25.50% | $18,856,168.56 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BIO/USDT:USDT | below_1h_threshold | +4.66% | +4.71% |
| TAG/USDT:USDT | below_1h_threshold | +4.33% | +4.37% |
| ORDI/USDT:USDT | below_1h_threshold | +3.53% | +3.58% |
| CHILLGUY/USDT:USDT | below_1h_threshold | +2.38% | +2.43% |
| RAVE/USDT:USDT | below_1h_threshold | +1.43% | +1.47% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
