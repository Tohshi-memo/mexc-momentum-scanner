# Decision Report

- generated_at: 2026-08-25T10:26:22.794145+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12595**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.80% / filled 20/20。**
- 全期間 MARKET基準: n=12595, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.80%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |
| LIMIT_5PCT | 7/20 | 35.0% | +1.02% | **+0.36%** |
| LIMIT_4PCT | 12/20 | 60.0% | +0.04% | **+0.02%** |
| LIMIT_1PCT | 17/20 | 85.0% | -0.04% | **-0.04%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | -0.35% | **-0.12%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 12/20 | 60.0% | +0.88% | **+0.53%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +1.26% | **+0.50%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +1.08% | **+0.43%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +1.06% | **+0.43%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +0.39% | **+0.25%** |

## 2. $100 Live Portfolio

- 残高: **$121.16** / 初期 $100.00 (+21.16%)
- 確定トレード: 192件 (TP 73 / SL 114 / EXP 5)
- 最新: CATE/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.16
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$702.01** / 初期 $100.00 (+602.01%)
- 確定: 4575件 (Win 1391 / Loss 1500 / Flat 1684) / skip 4581件
- 成長率目線: 平均log +0.000426 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: STX/USDT:USDT `LIMIT_4PCT_LONG` SL_HIT account -0.50% 残高後 $702.01

## 4. Robust Adaptive DryRun ($100)

- 残高: **$155.51** / 初期 $100.00 (+55.51%)
- 確定: 1977件 (Win 536 / Loss 473 / Flat 968) / skip 4029件
- 成長率目線: 平均log +0.000223 / 幾何平均 +0.022% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0347 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: PONS/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $155.51

## 5. Causal Adaptive DryRun ($100)

- 残高: **$115.47** / 初期 $100.00 (+15.47%)
- 確定: 1925件 (Win 564 / Loss 732 / Flat 629) / pending 5件 / skip 2137件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000201 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: STX/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $115.47

## 6. Latest Market Context

- 更新: 2026-08-25T10:26:13.741364+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.15% price=79280.0
- Funnel: target 1023 → liquid 178 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CATE/USDT:USDT | +79.27% | $4,755,011.04 |
| JIMOTHY/USDT:USDT | +58.72% | $1,330,198.86 |
| TAC/USDT:USDT | +39.33% | $6,231,257.89 |
| ONG/USDT:USDT | +35.08% | $7,336,850.07 |
| BR/USDT:USDT | +18.39% | $3,420,569.12 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| H/USDT:USDT | below_1h_threshold | +4.56% | +4.41% |
| TAC/USDT:USDT | below_1h_threshold | +3.97% | +3.82% |
| SNXX/USDT:USDT | below_1h_threshold | +3.01% | +2.86% |
| SOXL/USDT:USDT | below_1h_threshold | +2.03% | +1.88% |
| KORU/USDT:USDT | below_1h_threshold | +1.83% | +1.68% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
