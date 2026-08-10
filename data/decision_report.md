# Decision Report

- generated_at: 2026-08-10T23:51:19.246357+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11202**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.38% / filled 20/20。**
- 全期間 MARKET基準: n=11202, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.38%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.38% | **+0.38%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 3/20 | 15.0% | +8.00% | **+1.20%** |
| LIMIT_8PCT | 5/20 | 25.0% | +4.74% | **+1.19%** |
| LIMIT_7PCT | 6/20 | 30.0% | +3.40% | **+1.02%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +1.60% | **+0.64%** |
| LIMIT_9PCT | 3/20 | 15.0% | +2.86% | **+0.43%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.97% | **+0.87%** |
| MARKET_LONG | 20/20 | 100.0% | +0.87% | **+0.87%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +0.77% | **+0.58%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +0.67% | **+0.37%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +0.29% | **+0.18%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 176件 (TP 67 / SL 104 / EXP 5)
- 最新: AAOISTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$616.77** / 初期 $100.00 (+516.77%)
- 確定: 3936件 (Win 1230 / Loss 1285 / Flat 1421) / skip 3827件
- 成長率目線: 平均log +0.000462 / 幾何平均 +0.046% per trade / maxDD +8.13%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CASHCAT/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $616.77

## 4. Robust Adaptive DryRun ($100)

- 残高: **$141.89** / 初期 $100.00 (+41.89%)
- 確定: 1513件 (Win 424 / Loss 361 / Flat 728) / skip 3100件
- 成長率目線: 平均log +0.000231 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `LIMIT_FIB1272` (selected_by_robust_growth_score) / robust_score -0.0501 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: TST/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.08% 残高後 $141.89

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.30** / 初期 $100.00 (+17.30%)
- 確定: 1303件 (Win 404 / Loss 506 / Flat 393) / pending 1件 / skip 1370件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000101 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CHIP/USDT:USDT `MARKET` EXPIRED account +0.22% 残高後 $117.30

## 6. Latest Market Context

- 更新: 2026-08-10T23:51:10.918849+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.08% price=63936.6
- Funnel: target 962 → liquid 194 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BLUAI/USDT:USDT | +98.42% | $12,883,384.49 |
| BSPSTOCK/USDT:USDT | +10.91% | $1,144,528.32 |
| CYS/USDT:USDT | +9.54% | $27,130,990.20 |
| CRV/USDT:USDT | +9.53% | $7,870,023.37 |
| BTW/USDT:USDT | +8.49% | $7,780,451.20 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BLUAI/USDT:USDT | below_1h_threshold | +3.32% | +3.40% |
| LIT/USDT:USDT | below_1h_threshold | +1.37% | +1.45% |
| UAI/USDT:USDT | below_1h_threshold | +1.37% | +1.45% |
| BSPSTOCK/USDT:USDT | below_1h_threshold | +1.29% | +1.37% |
| ACE/USDT:USDT | below_1h_threshold | +1.27% | +1.35% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
