# Decision Report

- generated_at: 2026-09-16T11:01:26.371774+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14667**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=14667, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-1.64%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.64% | **-1.64%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 10/20 | 50.0% | +2.08% | **+1.04%** |
| LIMIT_ATR | 17/20 | 85.0% | +0.33% | **+0.28%** |
| LIMIT_7PCT | 5/20 | 25.0% | +1.12% | **+0.28%** |
| LIMIT_4PCT | 15/20 | 75.0% | +0.27% | **+0.20%** |
| LIMIT_BB3S | 4/9 | 44.4% | +0.25% | **+0.11%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +2.54% | **+2.16%** |
| LIMIT_BB3S_LONG | 6/11 | 54.5% | +3.14% | **+1.72%** |
| MARKET_LONG | 20/20 | 100.0% | +1.39% | **+1.39%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +1.82% | **+1.18%** |
| LIMIT_ATR_LONG | 10/20 | 50.0% | +1.67% | **+0.84%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 214件 (TP 79 / SL 130 / EXP 5)
- 最新: SHROOM/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,065.23** / 初期 $100.00 (+965.23%)
- 確定: 5545件 (Win 1653 / Loss 1791 / Flat 2101) / skip 5683件
- 成長率目線: 平均log +0.000427 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LSK/USDT:USDT `LIMIT_1PCT_LONG` TP_HIT account +1.00% 残高後 $1,065.23

## 4. Robust Adaptive DryRun ($100)

- 残高: **$230.59** / 初期 $100.00 (+130.59%)
- 確定: 3073件 (Win 844 / Loss 722 / Flat 1507) / skip 5005件
- 成長率目線: 平均log +0.000272 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0314 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: LSK/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.07% 残高後 $230.59

## 5. Causal Adaptive DryRun ($100)

- 残高: **$123.97** / 初期 $100.00 (+23.97%)
- 確定: 2954件 (Win 878 / Loss 1163 / Flat 913) / pending 2件 / skip 3184件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000176 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BR/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $123.97

## 6. Latest Market Context

- 更新: 2026-09-16T11:01:17.094979+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.11% price=76017.8
- Funnel: target 1058 → liquid 150 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SYN/USDT:USDT | +110.78% | $17,407,569.38 |
| LSK/USDT:USDT | +54.20% | $22,513,264.13 |
| BR/USDT:USDT | +39.52% | $17,456,477.51 |
| USELESS/USDT:USDT | +17.17% | $7,411,168.47 |
| LONGXIA/USDT:USDT | +12.56% | $2,642,644.08 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LSK/USDT:USDT | below_1h_threshold | +4.51% | +4.40% |
| BULLA/USDT:USDT | below_1h_threshold | +0.49% | +0.38% |
| LONGXIA/USDT:USDT | below_1h_threshold | +0.48% | +0.37% |
| USELESS/USDT:USDT | below_1h_threshold | +0.37% | +0.26% |
| NEAR/USDT:USDT | below_1h_threshold | +0.37% | +0.26% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
