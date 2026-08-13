# Decision Report

- generated_at: 2026-08-13T08:56:27.789836+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11432**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.20% / filled 20/20。**
- 全期間 MARKET基準: n=11432, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 2/20 | 10.0% | +7.96% | **+0.80%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.80% | **+0.76%** |
| LIMIT_BB3S | 4/20 | 20.0% | +3.12% | **+0.62%** |
| LIMIT_2PCT | 16/20 | 80.0% | +0.77% | **+0.62%** |
| LIMIT_3PCT | 15/20 | 75.0% | +0.82% | **+0.61%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 19/20 | 95.0% | +1.52% | **+1.45%** |
| LIMIT_3PCT_LONG | 16/20 | 80.0% | +1.80% | **+1.44%** |
| LIMIT_FIB1272_LONG | 14/20 | 70.0% | +1.84% | **+1.29%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +1.07% | **+1.02%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +1.05% | **+0.68%** |

## 2. $100 Live Portfolio

- 残高: **$121.65** / 初期 $100.00 (+21.65%)
- 確定トレード: 182件 (TP 71 / SL 106 / EXP 5)
- 最新: GUA/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.65
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$606.85** / 初期 $100.00 (+506.85%)
- 確定: 3951件 (Win 1233 / Loss 1292 / Flat 1426) / skip 4042件
- 成長率目線: 平均log +0.000456 / 幾何平均 +0.046% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: APR/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $606.85

## 4. Robust Adaptive DryRun ($100)

- 残高: **$148.93** / 初期 $100.00 (+48.93%)
- 確定: 1620件 (Win 460 / Loss 384 / Flat 776) / skip 3223件
- 成長率目線: 平均log +0.000246 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1386 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: COOKIE/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $148.93

## 5. Causal Adaptive DryRun ($100)

- 残高: **$115.89** / 初期 $100.00 (+15.89%)
- 確定: 1440件 (Win 423 / Loss 542 / Flat 475) / pending 3件 / skip 1460件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000181 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: COOKIE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $115.89

## 6. Latest Market Context

- 更新: 2026-08-13T08:56:19.644832+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.16% price=63731.5
- Funnel: target 973 → liquid 180 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ACU/USDT:USDT | +23.16% | $5,621,771.81 |
| APR/USDT:USDT | +16.18% | $16,024,320.21 |
| BTW/USDT:USDT | +14.41% | $29,359,573.40 |
| TST/USDT:USDT | +12.88% | $1,179,532.44 |
| COTI/USDT:USDT | +12.17% | $9,978,033.41 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AKE/USDT:USDT | below_1h_threshold | +4.61% | +4.77% |
| APR/USDT:USDT | below_1h_threshold | +3.15% | +3.31% |
| BR/USDT:USDT | below_1h_threshold | +3.00% | +3.16% |
| TST/USDT:USDT | below_1h_threshold | +2.79% | +2.95% |
| ZHIPUSTOCK/USDT:USDT | below_1h_threshold | +2.51% | +2.66% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
