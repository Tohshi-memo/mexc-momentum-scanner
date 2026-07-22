# Decision Report

- generated_at: 2026-07-22T04:01:16.670013+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9247**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9247, expectancy=-0.01%
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
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +2.62% | **+1.70%** |
| LIMIT_ATR_LONG | 8/20 | 40.0% | +0.99% | **+0.40%** |
| LIMIT_FIB1272_LONG | 2/20 | 10.0% | +3.51% | **+0.35%** |

## 2. $100 Live Portfolio

- 残高: **$104.85** / 初期 $100.00 (+4.85%)
- 確定トレード: 131件 (TP 44 / SL 82 / EXP 5)
- 最新: NIGHT/USDT:USDT SL_HIT PnL -4.00% 残高後 $104.85
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$419.29** / 初期 $100.00 (+319.29%)
- 確定: 3250件 (Win 1021 / Loss 1039 / Flat 1190) / skip 2558件
- 成長率目線: 平均log +0.000441 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BNCSTOCK/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $419.29

## 4. Robust Adaptive DryRun ($100)

- 残高: **$131.28** / 初期 $100.00 (+31.28%)
- 確定: 1159件 (Win 312 / Loss 252 / Flat 595) / skip 1499件
- 成長率目線: 平均log +0.000235 / 幾何平均 +0.023% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1678 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: RIF/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $131.28

## 5. Causal Adaptive DryRun ($100)

- 残高: **$102.74** / 初期 $100.00 (+2.74%)
- 確定: 391件 (Win 135 / Loss 159 / Flat 97) / pending 6件 / skip 325件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000419 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: LAB/USDT:USDT `MARKET_LONG` TP_HIT account +0.34% 残高後 $102.74

## 6. Latest Market Context

- 更新: 2026-07-22T04:01:09.947164+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.00% price=66177.8
- Funnel: target 885 → liquid 175 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| JIMOTHY/USDT:USDT | +43.24% | $4,189,367.99 |
| LAB/USDT:USDT | +33.55% | $7,082,562.30 |
| BANK/USDT:USDT | +21.98% | $121,194,919.78 |
| SMCISTOCK/USDT:USDT | +19.07% | $3,859,882.81 |
| PONS/USDT:USDT | +16.01% | $2,169,670.28 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LAB/USDT:USDT | below_1h_threshold | +3.24% | +3.24% |
| BANK/USDT:USDT | below_1h_threshold | +1.63% | +1.63% |
| ESPORTS/USDT:USDT | below_1h_threshold | +0.86% | +0.86% |
| PONS/USDT:USDT | below_1h_threshold | +0.73% | +0.72% |
| SPX/USDT:USDT | below_1h_threshold | +0.52% | +0.52% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
