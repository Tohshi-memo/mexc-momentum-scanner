# Decision Report

- generated_at: 2026-07-03T19:47:15.770368+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8189**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=8189, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.25%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.25% | **-0.25%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 4/20 | 20.0% | -0.15% | **-0.03%** |
| LIMIT_7PCT | 4/20 | 20.0% | -0.60% | **-0.12%** |
| LIMIT_1PCT | 17/20 | 85.0% | -0.24% | **-0.20%** |
| LIMIT_BB3S | 5/16 | 31.2% | -0.67% | **-0.21%** |
| LIMIT_5PCT | 6/20 | 30.0% | -0.70% | **-0.21%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +1.64% | **+1.64%** |
| MARKET_LONG | 20/20 | 100.0% | +1.60% | **+1.60%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +1.45% | **+0.72%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +0.71% | **+0.28%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +1.40% | **+0.14%** |

## 2. $100 Live Portfolio

- 残高: **$102.10** / 初期 $100.00 (+2.10%)
- 確定トレード: 57件 (TP 20 / SL 36 / EXP 1)
- 最新: VELVET/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.10
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$289.06** / 初期 $100.00 (+189.06%)
- 確定: 2508件 (Win 770 / Loss 834 / Flat 904) / skip 2242件
- 成長率目線: 平均log +0.000423 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: NOM/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $289.06

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.04** / 初期 $100.00 (+6.04%)
- 確定: 611件 (Win 147 / Loss 147 / Flat 317) / skip 989件
- 成長率目線: 平均log +0.000096 / 幾何平均 +0.010% per trade / maxDD +3.57%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BAS/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $106.04

## 5. Latest Market Context

- 更新: 2026-07-03T19:47:07.899123+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=62184.0
- Funnel: target 834 → liquid 162 → pre 50 → checked 50 → surge 3 → strict 2
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 75.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TLM/USDT:USDT | +51.24% | $18,695,683.64 |
| MAGMA/USDT:USDT | +35.84% | $10,707,291.19 |
| ANSEM/USDT:USDT | +33.67% | $1,463,303.02 |
| BAS/USDT:USDT | +18.05% | $3,289,280.10 |
| TA/USDT:USDT | +16.58% | $2,129,814.00 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MAGMA/USDT:USDT | below_1h_threshold | +4.95% | +4.95% |
| GPS/USDT:USDT | below_1h_threshold | +4.41% | +4.41% |
| US/USDT:USDT | below_1h_threshold | +4.16% | +4.16% |
| BASED/USDT:USDT | below_1h_threshold | +3.85% | +3.84% |
| HMSTR/USDT:USDT | below_1h_threshold | +2.94% | +2.94% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
