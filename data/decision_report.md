# Decision Report

- generated_at: 2026-06-22T18:20:39.809452+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7388**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.47% / filled 20/20。**
- 全期間 MARKET基準: n=7388, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.47%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.47% | **+0.47%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.49% | **+0.49%** |
| MARKET | 20/20 | 100.0% | +0.47% | **+0.47%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +0.97% | **+0.39%** |
| LIMIT_ATR | 13/20 | 65.0% | +0.59% | **+0.38%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.95% | **+0.29%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +0.53% | **+0.37%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +0.48% | **+0.31%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +0.32% | **+0.18%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +0.80% | **+0.16%** |
| ASK_LONG | 20/20 | 100.0% | +0.16% | **+0.16%** |

## 2. $100 Live Portfolio

- 残高: **$101.94** / 初期 $100.00 (+1.94%)
- 確定トレード: 29件 (TP 11 / SL 18 / EXP 0)
- 最新: RE/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.94
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$235.22** / 初期 $100.00 (+135.22%)
- 確定: 2044件 (Win 607 / Loss 672 / Flat 765) / skip 1905件
- 成長率目線: 平均log +0.000418 / 幾何平均 +0.042% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MMT/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $235.22

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.03** / 初期 $100.00 (+6.03%)
- 確定: 312件 (Win 89 / Loss 87 / Flat 136) / skip 487件
- 成長率目線: 平均log +0.000188 / 幾何平均 +0.019% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BTW/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $106.03

## 5. Latest Market Context

- 更新: 2026-06-22T18:20:35.026317+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.08% price=64629.1
- Funnel: target 808 → liquid 158 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| RE/USDT:USDT | +21.02% | $24,460,335.94 |
| SYN/USDT:USDT | +10.85% | $26,386,745.32 |
| BLESS/USDT:USDT | +9.96% | $4,775,225.12 |
| AAOISTOCK/USDT:USDT | +9.89% | $1,778,395.16 |
| NAORIS/USDT:USDT | +8.82% | $6,141,526.83 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MMT/USDT:USDT | below_1h_threshold | +1.92% | +1.84% |
| ARX/USDT:USDT | below_1h_threshold | +1.79% | +1.72% |
| HYPE/USDT:USDT | below_1h_threshold | +1.79% | +1.71% |
| JTO/USDT:USDT | below_1h_threshold | +1.67% | +1.59% |
| BLESS/USDT:USDT | below_1h_threshold | +1.42% | +1.34% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
