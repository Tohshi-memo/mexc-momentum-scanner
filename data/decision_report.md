# Decision Report

- generated_at: 2026-07-22T17:06:22.296557+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9297**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.50% / filled 20/20。**
- 全期間 MARKET基準: n=9297, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.50%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.50% | **+0.50%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT | 13/20 | 65.0% | +1.22% | **+0.79%** |
| LIMIT_ATR | 14/20 | 70.0% | +0.72% | **+0.51%** |
| MARKET | 20/20 | 100.0% | +0.50% | **+0.50%** |
| LIMIT_BB3S | 4/16 | 25.0% | +1.25% | **+0.31%** |
| LIMIT_FIB1272 | 13/20 | 65.0% | +0.39% | **+0.25%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 15/20 | 75.0% | +1.17% | **+0.88%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +0.51% | **+0.30%** |
| LIMIT_FIB1618_LONG | 6/20 | 30.0% | +0.39% | **+0.12%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +0.09% | **+0.05%** |
| LIMIT_BB3S_LONG | 4/4 | 100.0% | +0.02% | **+0.02%** |

## 2. $100 Live Portfolio

- 残高: **$105.90** / 初期 $100.00 (+5.90%)
- 確定トレード: 132件 (TP 45 / SL 82 / EXP 5)
- 最新: PROM/USDT:USDT TP_HIT PnL +8.00% 残高後 $105.90
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$431.91** / 初期 $100.00 (+331.91%)
- 確定: 3289件 (Win 1039 / Loss 1058 / Flat 1192) / skip 2569件
- 成長率目線: 平均log +0.000445 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SNXX/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $431.91

## 4. Robust Adaptive DryRun ($100)

- 残高: **$130.82** / 初期 $100.00 (+30.82%)
- 確定: 1160件 (Win 312 / Loss 253 / Flat 595) / skip 1548件
- 成長率目線: 平均log +0.000232 / 幾何平均 +0.023% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0671 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: LAB/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $130.82

## 5. Causal Adaptive DryRun ($100)

- 残高: **$101.55** / 初期 $100.00 (+1.55%)
- 確定: 425件 (Win 142 / Loss 176 / Flat 107) / pending 3件 / skip 349件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000135 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BLESS/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $101.55

## 6. Latest Market Context

- 更新: 2026-07-22T17:06:15.538474+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.02% price=66214.6
- Funnel: target 890 → liquid 182 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BROCCOLIF3B/USDT:USDT | +8.10% | $1,536,278.34 |
| BANK/USDT:USDT | +5.83% | $90,002,376.35 |
| RIF/USDT:USDT | +4.96% | $3,874,140.57 |
| WLD/USDT:USDT | +4.01% | $32,156,550.39 |
| AERO/USDT:USDT | +2.37% | $1,155,347.60 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ZHIPUSTOCK/USDT:USDT | below_1h_threshold | +2.19% | +2.16% |
| BANK/USDT:USDT | below_1h_threshold | +1.51% | +1.49% |
| SNXX/USDT:USDT | below_1h_threshold | +1.11% | +1.08% |
| UB/USDT:USDT | below_1h_threshold | +1.06% | +1.04% |
| KIOXIASTOCK/USDT:USDT | below_1h_threshold | +0.89% | +0.86% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
