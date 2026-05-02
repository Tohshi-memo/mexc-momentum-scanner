# Decision Report

- generated_at: 2026-05-02T18:37:13.624966+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2969**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=2969, expectancy=-0.17%
- 直近20件 MARKET基準: n=20, expectancy=+0.12%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.12% | **+0.12%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 20/20 | 100.0% | +1.03% | **+1.03%** |
| LIMIT_2PCT | 18/20 | 90.0% | +0.27% | **+0.24%** |
| ASK | 20/20 | 100.0% | +0.16% | **+0.16%** |
| MARKET | 20/20 | 100.0% | +0.12% | **+0.12%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.24% | **+0.09%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.23% | **+1.11%** |
| MARKET_LONG | 20/20 | 100.0% | +1.04% | **+1.04%** |
| ASK_LONG | 20/20 | 100.0% | +0.95% | **+0.95%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.02% | **+0.77%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +1.80% | **+0.72%** |

## 2. $100 Live Portfolio

- 残高: **$102.70** / 初期 $100.00 (+2.70%)
- 確定トレード: 9件 (TP 4 / SL 4 / EXP 1)
- 最新: RAVE/USDT:USDT EXPIRED PnL +5.55% 残高後 $102.70
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-02T18:37:09.222062+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.07% price=78415.0
- Funnel: target 755 → liquid 167 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BSB/USDT:USDT | +19.83% | $8,468,313.15 |
| TAC/USDT:USDT | +9.32% | $2,611,216.85 |
| BASED/USDT:USDT | +6.71% | $1,314,651.01 |
| BIANRENSHENG/USDT:USDT | +6.38% | $1,052,785.96 |
| PNUT/USDT:USDT | +5.86% | $1,626,981.46 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AIOT/USDT:USDT | below_1h_threshold | +4.21% | +4.14% |
| RLS/USDT:USDT | below_1h_threshold | +3.24% | +3.17% |
| LUNC/USDT:USDT | below_1h_threshold | +3.14% | +3.07% |
| CYS/USDT:USDT | below_1h_threshold | +2.44% | +2.37% |
| TAC/USDT:USDT | below_1h_threshold | +1.75% | +1.69% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
