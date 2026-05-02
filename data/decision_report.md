# Decision Report

- generated_at: 2026-05-02T06:47:03.736835+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2874**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=2874, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=-0.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.40% | **-0.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 3/20 | 15.0% | +8.00% | **+1.20%** |
| LIMIT_10PCT | 3/20 | 15.0% | +8.00% | **+1.20%** |
| LIMIT_BB3S | 7/19 | 36.8% | +2.46% | **+0.91%** |
| LIMIT_1PCT | 20/20 | 100.0% | +0.51% | **+0.51%** |
| LIMIT_8PCT | 3/20 | 15.0% | +2.57% | **+0.39%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.84% | **+1.57%** |
| MARKET_LONG | 20/20 | 100.0% | +1.20% | **+1.20%** |
| ASK_LONG | 20/20 | 100.0% | +1.13% | **+1.13%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +1.11% | **+0.72%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +1.10% | **+0.38%** |

## 2. $100 Live Portfolio

- 残高: **$102.51** / 初期 $100.00 (+2.51%)
- 確定トレード: 7件 (TP 4 / SL 3 / EXP 0)
- 最新: BIO/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.51
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-02T06:47:01.479496+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.07% price=78197.3
- Funnel: target 755 → liquid 169 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 78.9 >= 65=1, 4h RSI 72.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LAB/USDT:USDT | +116.01% | $66,018,717.13 |
| IRYS/USDT:USDT | +20.12% | $1,155,419.36 |
| BLESS/USDT:USDT | +14.16% | $2,118,168.92 |
| B/USDT:USDT | +12.47% | $78,198,681.09 |
| TAC/USDT:USDT | +10.88% | $1,024,723.71 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BIO/USDT:USDT | below_1h_threshold | +4.94% | +4.86% |
| TAG/USDT:USDT | below_1h_threshold | +4.12% | +4.05% |
| UB/USDT:USDT | below_1h_threshold | +2.95% | +2.88% |
| FIGHT/USDT:USDT | below_1h_threshold | +1.99% | +1.92% |
| PIPPIN/USDT:USDT | below_1h_threshold | +1.87% | +1.80% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
