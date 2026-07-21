# Decision Report

- generated_at: 2026-07-21T16:51:11.221237+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9195**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.34% / filled 20/20。**
- 全期間 MARKET基準: n=9195, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.34%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.34% | **+1.34%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 17/20 | 85.0% | +1.77% | **+1.51%** |
| MARKET | 20/20 | 100.0% | +1.34% | **+1.34%** |
| LIMIT_BB3S | 3/17 | 17.6% | +3.89% | **+0.69%** |
| LIMIT_2PCT | 13/20 | 65.0% | +0.83% | **+0.54%** |
| LIMIT_ATR | 8/20 | 40.0% | +0.48% | **+0.19%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +1.18% | **+0.59%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +1.10% | **+0.22%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +0.06% | **+0.02%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +0.00% | **+0.00%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | -0.09% | **-0.08%** |

## 2. $100 Live Portfolio

- 残高: **$106.97** / 初期 $100.00 (+6.97%)
- 確定トレード: 127件 (TP 44 / SL 78 / EXP 5)
- 最新: BANK/USDT:USDT SL_HIT PnL -4.00% 残高後 $106.97
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$419.29** / 初期 $100.00 (+319.29%)
- 確定: 3249件 (Win 1021 / Loss 1039 / Flat 1189) / skip 2507件
- 成長率目線: 平均log +0.000441 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: JIMOTHY/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account -0.12% 残高後 $419.29

## 4. Robust Adaptive DryRun ($100)

- 残高: **$131.74** / 初期 $100.00 (+31.74%)
- 確定: 1156件 (Win 312 / Loss 251 / Flat 593) / skip 1450件
- 成長率目線: 平均log +0.000238 / 幾何平均 +0.024% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0253 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BANK/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $131.74

## 5. Causal Adaptive DryRun ($100)

- 残高: **$100.98** / 初期 $100.00 (+0.98%)
- 確定: 351件 (Win 122 / Loss 155 / Flat 74) / pending 3件 / skip 314件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000117 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BANK/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $100.98

## 6. Latest Market Context

- 更新: 2026-07-21T16:51:04.646243+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.24% price=66490.0
- Funnel: target 885 → liquid 174 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| MUU/USDT:USDT | +4.50% | $1,232,452.41 |
| TLM/USDT:USDT | +4.08% | $1,329,126.44 |
| SNXX/USDT:USDT | +3.61% | $1,148,900.04 |
| BANK/USDT:USDT | +3.21% | $120,032,424.73 |
| RE/USDT:USDT | +3.16% | $1,198,519.82 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TLM/USDT:USDT | below_1h_threshold | +4.44% | +4.68% |
| RE/USDT:USDT | below_1h_threshold | +3.17% | +3.40% |
| B/USDT:USDT | below_1h_threshold | +3.12% | +3.36% |
| BANK/USDT:USDT | below_1h_threshold | +2.92% | +3.16% |
| ALLO/USDT:USDT | below_1h_threshold | +2.66% | +2.89% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
