# Decision Report

- generated_at: 2026-07-16T11:01:10.730580+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8802**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=8802, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.64%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.64% | **-0.64%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 8/20 | 40.0% | +0.95% | **+0.38%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_4PCT | 14/20 | 70.0% | +0.00% | **+0.00%** |
| LIMIT_ATR | 14/20 | 70.0% | -0.05% | **-0.04%** |
| LIMIT_FIB1272 | 10/20 | 50.0% | -0.44% | **-0.22%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/5 | 80.0% | +1.40% | **+1.12%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +1.58% | **+0.87%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +1.28% | **+0.64%** |
| LIMIT_ATR_LONG | 10/20 | 50.0% | +0.89% | **+0.44%** |
| LIMIT_8PCT_LONG | 5/20 | 25.0% | +1.60% | **+0.40%** |

## 2. $100 Live Portfolio

- 残高: **$106.87** / 初期 $100.00 (+6.87%)
- 確定トレード: 104件 (TP 38 / SL 64 / EXP 2)
- 最新: ROAM/USDT:USDT SL_HIT PnL -4.00% 残高後 $106.87
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$337.95** / 初期 $100.00 (+237.95%)
- 確定: 2917件 (Win 910 / Loss 945 / Flat 1062) / skip 2446件
- 成長率目線: 平均log +0.000417 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AKE/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.12% 残高後 $337.95

## 4. Robust Adaptive DryRun ($100)

- 残高: **$107.35** / 初期 $100.00 (+7.35%)
- 確定: 764件 (Win 176 / Loss 169 / Flat 419) / skip 1449件
- 成長率目線: 平均log +0.000093 / 幾何平均 +0.009% per trade / maxDD +3.89%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score -0.0013 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AKE/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.07% 残高後 $107.35

## 5. Causal Adaptive DryRun ($100)

- 残高: **$97.96** / 初期 $100.00 (-2.04%)
- 確定: 73件 (Win 21 / Loss 48 / Flat 4) / pending 3件 / skip 198件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000420 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: AKE/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $97.96

## 6. Latest Market Context

- 更新: 2026-07-16T11:01:04.478737+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.01% price=64180.0
- Funnel: target 875 → liquid 168 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AKE/USDT:USDT | +21.62% | $43,539,564.44 |
| ROAM/USDT:USDT | +20.25% | $5,949,319.78 |
| BANK/USDT:USDT | +17.47% | $2,995,176.61 |
| US/USDT:USDT | +16.54% | $16,149,985.39 |
| ESPORTS/USDT:USDT | +15.49% | $2,179,966.13 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AKE/USDT:USDT | below_1h_threshold | +0.73% | +0.75% |
| UNHSTOCK/USDT:USDT | below_1h_threshold | +0.66% | +0.67% |
| INTCSTOCK/USDT:USDT | below_1h_threshold | +0.65% | +0.66% |
| CAP/USDT:USDT | below_1h_threshold | +0.28% | +0.29% |
| ORDI/USDT:USDT | below_1h_threshold | +0.27% | +0.28% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
