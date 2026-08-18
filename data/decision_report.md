# Decision Report

- generated_at: 2026-08-18T09:31:22.868870+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11897**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.80% / filled 20/20。**
- 全期間 MARKET基準: n=11897, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.80%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT | 12/20 | 60.0% | +1.33% | **+0.80%** |
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |
| LIMIT_3PCT | 14/20 | 70.0% | +0.74% | **+0.51%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.51% | **+0.46%** |
| LIMIT_BB3S | 2/20 | 10.0% | +3.22% | **+0.32%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +5.24% | **+1.31%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +3.00% | **+1.20%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +2.33% | **+0.93%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +1.33% | **+0.73%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +1.92% | **+0.67%** |

## 2. $100 Live Portfolio

- 残高: **$121.41** / 初期 $100.00 (+21.41%)
- 確定トレード: 187件 (TP 72 / SL 110 / EXP 5)
- 最新: HEMI/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.41
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$619.02** / 初期 $100.00 (+519.02%)
- 確定: 4198件 (Win 1295 / Loss 1370 / Flat 1533) / skip 4260件
- 成長率目線: 平均log +0.000434 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CYS/USDT:USDT `LIMIT_FIB1272_LONG` SL_HIT account -0.50% 残高後 $619.02

## 4. Robust Adaptive DryRun ($100)

- 残高: **$155.25** / 初期 $100.00 (+55.25%)
- 確定: 1819件 (Win 502 / Loss 427 / Flat 890) / skip 3489件
- 成長率目線: 平均log +0.000242 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0093 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: NIULAI/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $155.25

## 5. Causal Adaptive DryRun ($100)

- 残高: **$118.25** / 初期 $100.00 (+18.25%)
- 確定: 1708件 (Win 510 / Loss 648 / Flat 550) / pending 5件 / skip 1656件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000369 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CYS/USDT:USDT `MARKET` TP_HIT account +0.34% 残高後 $118.25

## 6. Latest Market Context

- 更新: 2026-08-18T09:31:12.230499+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.21% price=64130.0
- Funnel: target 992 → liquid 179 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PRL/USDT:USDT | +19.34% | $3,183,754.88 |
| RED/USDT:USDT | +18.57% | $2,754,793.00 |
| SOXS/USDT:USDT | +13.87% | $8,165,380.76 |
| VVV/USDT:USDT | +12.46% | $4,487,662.95 |
| OPN/USDT:USDT | +12.26% | $1,238,600.58 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| HEMI/USDT:USDT | below_1h_threshold | +3.85% | +4.06% |
| SOXS/USDT:USDT | below_1h_threshold | +2.93% | +3.14% |
| EDEN/USDT:USDT | below_1h_threshold | +2.85% | +3.06% |
| SKYAI/USDT:USDT | below_1h_threshold | +2.51% | +2.72% |
| NIULAI/USDT:USDT | below_1h_threshold | +1.90% | +2.11% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
