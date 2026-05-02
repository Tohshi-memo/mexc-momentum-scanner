# Decision Report

- generated_at: 2026-05-02T16:27:15.623861+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2955**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=2955, expectancy=-0.17%
- 直近20件 MARKET基準: n=20, expectancy=-1.05%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.05% | **-1.05%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 3/20 | 15.0% | +2.27% | **+0.34%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +1.20% | **+0.30%** |
| LIMIT_8PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_9PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_10PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +2.47% | **+1.85%** |
| LIMIT_BB3S_LONG | 5/7 | 71.4% | +2.59% | **+1.85%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +2.92% | **+1.75%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +2.24% | **+1.35%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.17% | **+0.99%** |

## 2. $100 Live Portfolio

- 残高: **$101.99** / 初期 $100.00 (+1.99%)
- 確定トレード: 8件 (TP 4 / SL 4 / EXP 0)
- 最新: NAORIS/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.99
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-02T16:27:05.728757+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.02% price=78467.5
- Funnel: target 755 → liquid 162 → pre 50 → checked 50 → surge 7 → strict 3
- Surge前reject: below_1h_threshold=43, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 88.2 >= 65=1, 4h RSI 97.0 >= 65=1, 4h RSI 87.0 >= 65=1, 4h RSI 78.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TAG/USDT:USDT | +33.82% | $12,175,488.89 |
| LAB/USDT:USDT | +19.92% | $186,108,559.50 |
| ORDI/USDT:USDT | +10.28% | $23,135,130.03 |
| TAC/USDT:USDT | +6.81% | $2,463,847.53 |
| BASED/USDT:USDT | +6.11% | $1,245,091.46 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PNUT/USDT:USDT | below_1h_threshold | +3.32% | +3.30% |
| CHILLGUY/USDT:USDT | below_1h_threshold | +2.71% | +2.69% |
| UB/USDT:USDT | below_1h_threshold | +2.58% | +2.56% |
| PLAY/USDT:USDT | below_1h_threshold | +2.57% | +2.55% |
| NAORIS/USDT:USDT | below_1h_threshold | +2.03% | +2.01% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
