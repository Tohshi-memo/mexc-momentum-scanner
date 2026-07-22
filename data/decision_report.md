# Decision Report

- generated_at: 2026-07-22T04:06:21.496038+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9248**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9248, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.99%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.99% | **-0.99%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 4/20 | 20.0% | +6.79% | **+1.36%** |
| LIMIT_8PCT | 6/20 | 30.0% | +1.18% | **+0.35%** |
| LIMIT_7PCT | 7/20 | 35.0% | +0.90% | **+0.31%** |
| LIMIT_FIB1618 | 3/20 | 15.0% | +1.23% | **+0.18%** |
| LIMIT_9PCT | 4/20 | 20.0% | +0.36% | **+0.07%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +3.17% | **+3.17%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +3.33% | **+2.99%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +2.33% | **+1.40%** |
| LIMIT_ATR_LONG | 8/20 | 40.0% | +0.99% | **+0.40%** |
| LIMIT_FIB1272_LONG | 2/20 | 10.0% | +3.51% | **+0.35%** |

## 2. $100 Live Portfolio

- 残高: **$104.85** / 初期 $100.00 (+4.85%)
- 確定トレード: 131件 (TP 44 / SL 82 / EXP 5)
- 最新: NIGHT/USDT:USDT SL_HIT PnL -4.00% 残高後 $104.85
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$421.94** / 初期 $100.00 (+321.94%)
- 確定: 3251件 (Win 1022 / Loss 1039 / Flat 1190) / skip 2558件
- 成長率目線: 平均log +0.000443 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LAB/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $421.94

## 4. Robust Adaptive DryRun ($100)

- 残高: **$131.28** / 初期 $100.00 (+31.28%)
- 確定: 1159件 (Win 312 / Loss 252 / Flat 595) / skip 1500件
- 成長率目線: 平均log +0.000235 / 幾何平均 +0.023% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1858 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: RIF/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $131.28

## 5. Causal Adaptive DryRun ($100)

- 残高: **$102.92** / 初期 $100.00 (+2.92%)
- 確定: 392件 (Win 136 / Loss 159 / Flat 97) / pending 5件 / skip 325件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000462 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: LAB/USDT:USDT `MARKET_LONG` EXPIRED account +0.17% 残高後 $102.92

## 6. Latest Market Context

- 更新: 2026-07-22T04:06:13.413287+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.18% price=66296.9
- Funnel: target 885 → liquid 175 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| JIMOTHY/USDT:USDT | +38.22% | $4,201,257.35 |
| LAB/USDT:USDT | +33.62% | $7,333,664.46 |
| BANK/USDT:USDT | +22.10% | $121,439,641.56 |
| SMCISTOCK/USDT:USDT | +19.22% | $3,880,318.88 |
| RE/USDT:USDT | +15.74% | $1,941,492.82 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LAB/USDT:USDT | below_1h_threshold | +3.53% | +3.35% |
| AKE/USDT:USDT | below_1h_threshold | +1.75% | +1.56% |
| BANK/USDT:USDT | below_1h_threshold | +1.64% | +1.46% |
| ESPORTS/USDT:USDT | below_1h_threshold | +1.45% | +1.26% |
| NIGHT/USDT:USDT | below_1h_threshold | +1.16% | +0.97% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
