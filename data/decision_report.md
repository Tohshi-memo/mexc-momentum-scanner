# Decision Report

- generated_at: 2026-09-22T20:16:24.444308+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15357**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=15357, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-2.48%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.48% | **-2.48%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 4/20 | 20.0% | +0.42% | **+0.08%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.13% | **+0.04%** |
| LIMIT_7PCT | 2/20 | 10.0% | -0.60% | **-0.06%** |
| LIMIT_3PCT | 16/20 | 80.0% | -0.18% | **-0.14%** |
| LIMIT_4PCT | 13/20 | 65.0% | -0.31% | **-0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/4 | 50.0% | +6.33% | **+3.16%** |
| MARKET_LONG | 20/20 | 100.0% | +1.36% | **+1.36%** |
| LIMIT_1PCT_LONG | 12/20 | 60.0% | +2.23% | **+1.34%** |
| LIMIT_4PCT_LONG | 6/20 | 30.0% | +4.00% | **+1.20%** |
| LIMIT_3PCT_LONG | 6/20 | 30.0% | +3.74% | **+1.12%** |

## 2. $100 Live Portfolio

- 残高: **$120.44** / 初期 $100.00 (+20.44%)
- 確定トレード: 216件 (TP 79 / SL 132 / EXP 5)
- 最新: PIEVERSE/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.44
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,155.90** / 初期 $100.00 (+1055.90%)
- 確定: 5841件 (Win 1728 / Loss 1878 / Flat 2235) / skip 6077件
- 成長率目線: 平均log +0.000419 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: TIA/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $1,155.90

## 4. Robust Adaptive DryRun ($100)

- 残高: **$249.51** / 初期 $100.00 (+149.51%)
- 確定: 3353件 (Win 926 / Loss 781 / Flat 1646) / skip 5415件
- 成長率目線: 平均log +0.000273 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: KERNEL/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $249.51

## 5. Causal Adaptive DryRun ($100)

- 残高: **$121.94** / 初期 $100.00 (+21.94%)
- 確定: 3112件 (Win 913 / Loss 1221 / Flat 978) / pending 4件 / skip 3720件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000091 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: KIOXIASTOCK/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $121.94

## 6. Latest Market Context

- 更新: 2026-09-22T20:16:15.634964+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.05% price=86186.5
- Funnel: target 1058 → liquid 186 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| DRIFT/USDT:USDT | +32.76% | $1,325,860.99 |
| 4/USDT:USDT | +17.67% | $1,845,996.62 |
| MUBARAK/USDT:USDT | +14.71% | $15,479,357.14 |
| BR/USDT:USDT | +14.62% | $6,252,571.01 |
| CHR/USDT:USDT | +13.29% | $4,206,380.65 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| USELESS/USDT:USDT | below_1h_threshold | +2.69% | +2.64% |
| KORU/USDT:USDT | below_1h_threshold | +1.84% | +1.79% |
| AIN/USDT:USDT | below_1h_threshold | +1.82% | +1.76% |
| SOXL/USDT:USDT | below_1h_threshold | +1.51% | +1.45% |
| UNI/USDT:USDT | below_1h_threshold | +1.40% | +1.34% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
