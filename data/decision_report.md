# Decision Report

- generated_at: 2026-05-02T16:22:08.145701+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2951**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=2951, expectancy=-0.17%
- 直近20件 MARKET基準: n=20, expectancy=-0.98%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.98% | **-0.98%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 5/20 | 25.0% | +4.56% | **+1.14%** |
| LIMIT_8PCT | 4/20 | 20.0% | +3.93% | **+0.79%** |
| LIMIT_6PCT | 7/20 | 35.0% | +1.08% | **+0.38%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +0.50% | **+0.20%** |
| LIMIT_9PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +3.19% | **+2.71%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +3.59% | **+2.52%** |
| LIMIT_ATR_LONG | 15/20 | 75.0% | +3.34% | **+2.51%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.83% | **+1.65%** |
| MARKET_LONG | 20/20 | 100.0% | +1.22% | **+1.22%** |

## 2. $100 Live Portfolio

- 残高: **$101.99** / 初期 $100.00 (+1.99%)
- 確定トレード: 8件 (TP 4 / SL 4 / EXP 0)
- 最新: NAORIS/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.99
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-02T16:22:03.294842+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.10% price=78530.5
- Funnel: target 755 → liquid 162 → pre 50 → checked 50 → surge 5 → strict 1
- Surge前reject: below_1h_threshold=45, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 87.8 >= 65=2, 4h RSI 96.9 >= 65=1, 4h RSI 79.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TAG/USDT:USDT | +30.95% | $11,736,356.22 |
| LAB/USDT:USDT | +16.19% | $183,245,892.56 |
| ORDI/USDT:USDT | +12.72% | $22,312,109.23 |
| PHAROS/USDT:USDT | +8.27% | $1,230,068.33 |
| XNY/USDT:USDT | +6.15% | $1,176,285.93 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TAC/USDT:USDT | below_1h_threshold | +4.55% | +4.45% |
| BASED/USDT:USDT | below_1h_threshold | +4.35% | +4.25% |
| PNUT/USDT:USDT | below_1h_threshold | +4.16% | +4.05% |
| CHILLGUY/USDT:USDT | below_1h_threshold | +3.83% | +3.72% |
| UB/USDT:USDT | below_1h_threshold | +3.77% | +3.67% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
