# Decision Report

- generated_at: 2026-08-11T03:41:44.414027+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11217**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.97% / filled 20/20。**
- 全期間 MARKET基準: n=11217, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.97%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.97% | **+0.97%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 3/20 | 15.0% | +8.00% | **+1.20%** |
| MARKET | 20/20 | 100.0% | +0.97% | **+0.97%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +0.05% | **+0.01%** |
| LIMIT_8PCT | 3/20 | 15.0% | -0.00% | **-0.00%** |
| LIMIT_9PCT | 3/20 | 15.0% | -0.00% | **-0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT_LONG | 11/20 | 55.0% | +0.64% | **+0.35%** |
| LIMIT_FIB1618_LONG | 5/20 | 25.0% | +0.84% | **+0.21%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +0.30% | **+0.18%** |
| LIMIT_5PCT_LONG | 11/20 | 55.0% | -0.00% | **-0.00%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | -0.22% | **-0.21%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 176件 (TP 67 / SL 104 / EXP 5)
- 最新: AAOISTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$616.77** / 初期 $100.00 (+516.77%)
- 確定: 3936件 (Win 1230 / Loss 1285 / Flat 1421) / skip 3842件
- 成長率目線: 平均log +0.000462 / 幾何平均 +0.046% per trade / maxDD +8.13%
- 次の候補: `見送り` (no_strategy_passed_safety_filters) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CASHCAT/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $616.77

## 4. Robust Adaptive DryRun ($100)

- 残高: **$141.89** / 初期 $100.00 (+41.89%)
- 確定: 1514件 (Win 424 / Loss 361 / Flat 729) / skip 3114件
- 成長率目線: 平均log +0.000231 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BLUAI/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $141.89

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.66** / 初期 $100.00 (+16.66%)
- 確定: 1315件 (Win 407 / Loss 515 / Flat 393) / pending 5件 / skip 1371件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000172 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BICO/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $116.66

## 6. Latest Market Context

- 更新: 2026-08-11T03:41:26.699671+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.17% price=64120.7
- Funnel: target 962 → liquid 187 → pre 50 → checked 50 → surge 3 → strict 3
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BLUAI/USDT:USDT | +82.81% | $16,421,842.06 |
| TOAD/USDT:USDT | +43.44% | $1,206,614.45 |
| CYS/USDT:USDT | +14.90% | $23,962,762.40 |
| CRV/USDT:USDT | +13.11% | $9,384,067.86 |
| BICO/USDT:USDT | +10.64% | $10,377,589.83 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CAP/USDT:USDT | below_1h_threshold | +4.83% | +4.66% |
| HEI/USDT:USDT | below_1h_threshold | +4.33% | +4.16% |
| EPIC/USDT:USDT | below_1h_threshold | +3.79% | +3.62% |
| LIGHT/USDT:USDT | below_1h_threshold | +3.20% | +3.03% |
| COOKIE/USDT:USDT | below_1h_threshold | +3.05% | +2.89% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
