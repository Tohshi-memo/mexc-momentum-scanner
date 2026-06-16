# Decision Report

- generated_at: 2026-06-16T18:36:03.039011+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6878**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6878, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-0.28%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.28% | **-0.28%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 5/20 | 25.0% | +0.96% | **+0.24%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +0.46% | **+0.14%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.00% | **+0.00%** |
| MARKET | 20/20 | 100.0% | -0.28% | **-0.28%** |
| ASK | 20/20 | 100.0% | -0.29% | **-0.29%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 5/6 | 83.3% | +3.01% | **+2.51%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.52% | **+1.14%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +1.28% | **+0.77%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +0.82% | **+0.66%** |
| ASK_LONG | 20/20 | 100.0% | +0.50% | **+0.50%** |

## 2. $100 Live Portfolio

- 残高: **$101.99** / 初期 $100.00 (+1.99%)
- 確定トレード: 11件 (TP 5 / SL 6 / EXP 0)
- 最新: STG/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.99
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$185.89** / 初期 $100.00 (+85.89%)
- 確定: 1751件 (Win 462 / Loss 549 / Flat 740) / skip 1688件
- 成長率目線: 平均log +0.000354 / 幾何平均 +0.035% per trade / maxDD +7.25%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $185.89

## 4. Robust Adaptive DryRun ($100)

- 残高: **$97.60** / 初期 $100.00 (-2.40%)
- 確定: 156件 (Win 28 / Loss 30 / Flat 98) / skip 133件
- 成長率目線: 平均log -0.000155 / 幾何平均 -0.016% per trade / maxDD +3.03%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0432 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: VELVET/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $97.60

## 5. Latest Market Context

- 更新: 2026-06-16T18:35:55.922003+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.14% price=65856.0
- Funnel: target 782 → liquid 158 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| H/USDT:USDT | +14.48% | $61,719,952.17 |
| VELVET/USDT:USDT | +13.59% | $25,350,260.34 |
| ESPORTS/USDT:USDT | +9.13% | $1,634,498.83 |
| STG/USDT:USDT | +8.42% | $3,536,869.63 |
| UNI/USDT:USDT | +6.35% | $36,149,113.99 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ESPORTS/USDT:USDT | below_1h_threshold | +3.49% | +3.63% |
| UAI/USDT:USDT | below_1h_threshold | +2.69% | +2.83% |
| RIVER/USDT:USDT | below_1h_threshold | +1.94% | +2.07% |
| XMR/USDT:USDT | below_1h_threshold | +1.67% | +1.81% |
| VVV/USDT:USDT | below_1h_threshold | +1.64% | +1.78% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
