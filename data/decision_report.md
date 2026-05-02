# Decision Report

- generated_at: 2026-05-02T15:34:30.166922+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2931**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=2931, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=-2.52%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.52% | **-2.52%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 8/20 | 40.0% | +3.42% | **+1.37%** |
| LIMIT_7PCT | 4/20 | 20.0% | +5.40% | **+1.08%** |
| LIMIT_8PCT | 3/20 | 15.0% | +6.57% | **+0.99%** |
| LIMIT_5PCT | 13/20 | 65.0% | +1.27% | **+0.83%** |
| LIMIT_9PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/3 | 100.0% | +6.62% | **+6.62%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.38% | **+1.24%** |
| MARKET_LONG | 20/20 | 100.0% | +1.14% | **+1.14%** |
| LIMIT_5PCT_LONG | 7/20 | 35.0% | +2.98% | **+1.04%** |
| ASK_LONG | 20/20 | 100.0% | +0.82% | **+0.82%** |

## 2. $100 Live Portfolio

- 残高: **$101.99** / 初期 $100.00 (+1.99%)
- 確定トレード: 8件 (TP 4 / SL 4 / EXP 0)
- 最新: NAORIS/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.99
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-02T15:34:27.486978+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.03% price=78356.7
- Funnel: target 755 → liquid 161 → pre 50 → checked 50 → surge 4 → strict 0
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 86.7 >= 65=1, 4h RSI 81.7 >= 65=1, 4h RSI 76.4 >= 65=1, 4h RSI 96.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LAB/USDT:USDT | +315.55% | $166,334,025.39 |
| TAG/USDT:USDT | +70.82% | $10,103,407.04 |
| BIO/USDT:USDT | +45.05% | $3,952,687.97 |
| SKYAI/USDT:USDT | +37.49% | $19,307,087.34 |
| ORDI/USDT:USDT | +26.91% | $15,270,864.14 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TAG/USDT:USDT | below_1h_threshold | +4.46% | +4.49% |
| KNC/USDT:USDT | below_1h_threshold | +3.74% | +3.77% |
| B/USDT:USDT | below_1h_threshold | +3.12% | +3.15% |
| UB/USDT:USDT | below_1h_threshold | +1.93% | +1.96% |
| XNY/USDT:USDT | below_1h_threshold | +1.70% | +1.73% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
