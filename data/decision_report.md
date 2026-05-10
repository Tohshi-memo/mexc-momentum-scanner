# Decision Report

- generated_at: 2026-05-10T18:10:31.808037+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3978**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3978, expectancy=-0.13%
- 直近20件 MARKET基準: n=20, expectancy=-2.07%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.07% | **-2.07%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 5/20 | 25.0% | +0.95% | **+0.24%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +0.94% | **+0.09%** |
| LIMIT_FIB1272 | 11/20 | 55.0% | +0.09% | **+0.05%** |
| LIMIT_4PCT | 14/20 | 70.0% | +0.03% | **+0.02%** |
| LIMIT_BB3S | 3/15 | 20.0% | +0.09% | **+0.02%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 12/20 | 60.0% | +3.05% | **+1.83%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +3.65% | **+1.82%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +1.94% | **+1.55%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +3.74% | **+1.50%** |
| LIMIT_4PCT_LONG | 8/20 | 40.0% | +3.54% | **+1.41%** |

## 2. $100 Live Portfolio

- 残高: **$98.21** / 初期 $100.00 (-1.79%)
- 確定トレード: 30件 (TP 7 / SL 20 / EXP 3)
- 最新: SATO/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.21
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$107.73** / 初期 $100.00 (+7.73%)
- 確定: 198件 (Win 48 / Loss 66 / Flat 84) / skip 341件
- 成長率目線: 平均log +0.000376 / 幾何平均 +0.038% per trade / maxDD +4.09%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BILL/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $107.73

## 4. Latest Market Context

- 更新: 2026-05-10T18:10:28.693032+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.07% price=81384.0
- Funnel: target 769 → liquid 163 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| B/USDT:USDT | +14.22% | $1,454,777.17 |
| DEEP/USDT:USDT | +10.67% | $1,287,667.31 |
| TRUTH/USDT:USDT | +9.35% | $2,062,577.83 |
| SUI/USDT:USDT | +9.22% | $502,196,933.54 |
| 1000BONK/USDT:USDT | +7.75% | $13,547,049.97 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CAKE/USDT:USDT | below_1h_threshold | +1.72% | +1.79% |
| 1000BONK/USDT:USDT | below_1h_threshold | +1.16% | +1.23% |
| TRUTH/USDT:USDT | below_1h_threshold | +1.14% | +1.21% |
| DEEP/USDT:USDT | below_1h_threshold | +1.01% | +1.08% |
| BSB/USDT:USDT | below_1h_threshold | +0.80% | +0.87% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
