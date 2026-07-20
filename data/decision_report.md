# Decision Report

- generated_at: 2026-07-20T18:06:16.917002+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9122**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9122, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-2.02%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.02% | **-2.02%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 3/20 | 15.0% | +4.54% | **+0.68%** |
| LIMIT_8PCT | 2/20 | 10.0% | +5.85% | **+0.59%** |
| LIMIT_6PCT | 6/20 | 30.0% | +0.91% | **+0.27%** |
| LIMIT_5PCT | 10/20 | 50.0% | +0.46% | **+0.23%** |
| LIMIT_BB3S | 4/12 | 33.3% | -0.54% | **-0.18%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.64% | **+1.39%** |
| LIMIT_3PCT_LONG | 8/20 | 40.0% | +3.40% | **+1.36%** |
| MARKET_LONG | 20/20 | 100.0% | +1.22% | **+1.22%** |
| LIMIT_ATR_LONG | 10/20 | 50.0% | +2.22% | **+1.11%** |
| LIMIT_4PCT_LONG | 7/20 | 35.0% | +2.86% | **+1.00%** |

## 2. $100 Live Portfolio

- 残高: **$109.14** / 初期 $100.00 (+9.14%)
- 確定トレード: 123件 (TP 44 / SL 74 / EXP 5)
- 最新: US/USDT:USDT TP_HIT PnL +8.00% 残高後 $109.14
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$405.90** / 初期 $100.00 (+305.90%)
- 確定: 3184件 (Win 995 / Loss 1009 / Flat 1180) / skip 2499件
- 成長率目線: 平均log +0.000440 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ON/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $405.90

## 4. Robust Adaptive DryRun ($100)

- 残高: **$127.25** / 初期 $100.00 (+27.25%)
- 確定: 1083件 (Win 281 / Loss 219 / Flat 583) / skip 1450件
- 成長率目線: 平均log +0.000223 / 幾何平均 +0.022% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1201 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ON/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $127.25

## 5. Causal Adaptive DryRun ($100)

- 残高: **$101.85** / 初期 $100.00 (+1.85%)
- 確定: 320件 (Win 112 / Loss 139 / Flat 69) / pending 6件 / skip 270件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000359 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: APDSTOCK/USDT:USDT `MARKET_LONG` EXPIRED account +0.01% 残高後 $101.85

## 6. Latest Market Context

- 更新: 2026-07-20T18:06:10.927454+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.04% price=65587.5
- Funnel: target 885 → liquid 159 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| UB/USDT:USDT | +6.35% | $1,135,404.66 |
| ON/USDT:USDT | +6.00% | $1,407,095.67 |
| ESPORTS/USDT:USDT | +5.22% | $9,173,705.95 |
| USELESS/USDT:USDT | +5.20% | $1,046,247.43 |
| LDO/USDT:USDT | +5.07% | $2,437,514.65 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AXONSTOCK/USDT:USDT | below_1h_threshold | +2.31% | +2.27% |
| UB/USDT:USDT | below_1h_threshold | +1.86% | +1.81% |
| ESPORTS/USDT:USDT | below_1h_threshold | +1.48% | +1.44% |
| INFQSTOCK/USDT:USDT | below_1h_threshold | +1.41% | +1.36% |
| CRCLSTOCK/USDT:USDT | below_1h_threshold | +1.37% | +1.33% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
