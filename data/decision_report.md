# Decision Report

- generated_at: 2026-06-20T21:24:04.063241+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7272**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7272, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-1.54%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.54% | **-1.54%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 2/20 | 10.0% | +6.29% | **+0.63%** |
| LIMIT_8PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_7PCT | 4/20 | 20.0% | +2.40% | **+0.48%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +4.10% | **+0.41%** |
| LIMIT_6PCT | 6/20 | 30.0% | +0.91% | **+0.27%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.94% | **+1.94%** |
| ASK_LONG | 20/20 | 100.0% | +1.24% | **+1.24%** |
| LIMIT_ATR_LONG | 8/20 | 40.0% | +1.44% | **+0.58%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.22% | **+0.22%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +1.10% | **+0.16%** |

## 2. $100 Live Portfolio

- 残高: **$101.45** / 初期 $100.00 (+1.45%)
- 確定トレード: 24件 (TP 9 / SL 15 / EXP 0)
- 最新: VELVET/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.45
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$238.63** / 初期 $100.00 (+138.63%)
- 確定: 2001件 (Win 591 / Loss 652 / Flat 758) / skip 1832件
- 成長率目線: 平均log +0.000435 / 幾何平均 +0.043% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PIPPIN/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $238.63

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.03** / 初期 $100.00 (+6.03%)
- 確定: 310件 (Win 89 / Loss 87 / Flat 134) / skip 373件
- 成長率目線: 平均log +0.000189 / 幾何平均 +0.019% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BLESS/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $106.03

## 5. Latest Market Context

- 更新: 2026-06-20T21:23:59.617349+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.02% price=63909.6
- Funnel: target 796 → liquid 134 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BICO/USDT:USDT | +40.91% | $45,885,818.37 |
| ALICE/USDT:USDT | +19.07% | $1,686,657.06 |
| VELVET/USDT:USDT | +10.06% | $16,706,016.20 |
| ASTEROID/USDT:USDT | +9.12% | $1,581,206.03 |
| AGT/USDT:USDT | +5.98% | $2,521,384.58 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ALICE/USDT:USDT | below_1h_threshold | +4.91% | +4.90% |
| AXS/USDT:USDT | below_1h_threshold | +2.18% | +2.16% |
| SKYAI/USDT:USDT | below_1h_threshold | +1.67% | +1.66% |
| JUP/USDT:USDT | below_1h_threshold | +1.23% | +1.21% |
| AERO/USDT:USDT | below_1h_threshold | +1.17% | +1.15% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
