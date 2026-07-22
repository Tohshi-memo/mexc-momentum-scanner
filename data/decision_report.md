# Decision Report

- generated_at: 2026-07-22T12:16:19.711647+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9281**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.28% / filled 20/20。**
- 全期間 MARKET基準: n=9281, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.28%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.28% | **+0.28%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 2/20 | 10.0% | +5.85% | **+0.59%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.80% | **+0.42%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |
| LIMIT_ATR | 10/20 | 50.0% | +0.67% | **+0.33%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +0.93% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 5/5 | 100.0% | +1.00% | **+1.00%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +0.81% | **+0.57%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +0.57% | **+0.54%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +0.33% | **+0.18%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +0.12% | **+0.06%** |

## 2. $100 Live Portfolio

- 残高: **$104.85** / 初期 $100.00 (+4.85%)
- 確定トレード: 131件 (TP 44 / SL 82 / EXP 5)
- 最新: NIGHT/USDT:USDT SL_HIT PnL -4.00% 残高後 $104.85
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$433.95** / 初期 $100.00 (+333.95%)
- 確定: 3278件 (Win 1035 / Loss 1052 / Flat 1191) / skip 2564件
- 成長率目線: 平均log +0.000448 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AKE/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $433.95

## 4. Robust Adaptive DryRun ($100)

- 残高: **$130.82** / 初期 $100.00 (+30.82%)
- 確定: 1160件 (Win 312 / Loss 253 / Flat 595) / skip 1532件
- 成長率目線: 平均log +0.000232 / 幾何平均 +0.023% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1258 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: LAB/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $130.82

## 5. Causal Adaptive DryRun ($100)

- 残高: **$102.44** / 初期 $100.00 (+2.44%)
- 確定: 418件 (Win 142 / Loss 171 / Flat 105) / pending 3件 / skip 332件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000320 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: AKE/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $102.44

## 6. Latest Market Context

- 更新: 2026-07-22T12:16:15.106137+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.12% price=65901.5
- Funnel: target 888 → liquid 178 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| JIMOTHY/USDT:USDT | +46.57% | $3,337,883.09 |
| RE/USDT:USDT | +28.05% | $10,065,594.91 |
| SMCISTOCK/USDT:USDT | +16.28% | $4,547,443.75 |
| UB/USDT:USDT | +16.22% | $1,660,166.18 |
| BLESS/USDT:USDT | +14.27% | $1,055,496.98 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BLESS/USDT:USDT | below_1h_threshold | +3.50% | +3.62% |
| INFQSTOCK/USDT:USDT | below_1h_threshold | +3.37% | +3.49% |
| ERA/USDT:USDT | below_1h_threshold | +1.53% | +1.65% |
| BANK/USDT:USDT | below_1h_threshold | +1.32% | +1.44% |
| PONS/USDT:USDT | below_1h_threshold | +1.25% | +1.37% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
