# Decision Report

- generated_at: 2026-08-12T17:11:28.249480+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11386**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.41% / filled 20/20。**
- 全期間 MARKET基準: n=11386, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.41%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.41% | **+1.41%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.41% | **+1.41%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.90% | **+0.81%** |
| LIMIT_2PCT | 16/20 | 80.0% | +0.91% | **+0.73%** |
| LIMIT_BB3S | 5/18 | 27.8% | +2.06% | **+0.57%** |
| LIMIT_7PCT | 2/20 | 10.0% | +5.40% | **+0.54%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +1.07% | **+1.01%** |
| LIMIT_10PCT_LONG | 5/20 | 25.0% | +3.38% | **+0.84%** |
| LIMIT_FIB1272_LONG | 6/20 | 30.0% | +0.53% | **+0.16%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +0.17% | **+0.13%** |
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +0.25% | **+0.07%** |

## 2. $100 Live Portfolio

- 残高: **$121.65** / 初期 $100.00 (+21.65%)
- 確定トレード: 182件 (TP 71 / SL 106 / EXP 5)
- 最新: GUA/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.65
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$606.08** / 初期 $100.00 (+506.08%)
- 確定: 3948件 (Win 1232 / Loss 1291 / Flat 1425) / skip 3999件
- 成長率目線: 平均log +0.000456 / 幾何平均 +0.046% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ACE/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $606.08

## 4. Robust Adaptive DryRun ($100)

- 残高: **$147.30** / 初期 $100.00 (+47.30%)
- 確定: 1596件 (Win 449 / Loss 374 / Flat 773) / skip 3201件
- 成長率目線: 平均log +0.000243 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0446 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BR/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $147.30

## 5. Causal Adaptive DryRun ($100)

- 残高: **$115.00** / 初期 $100.00 (+15.00%)
- 確定: 1399件 (Win 416 / Loss 535 / Flat 448) / pending 6件 / skip 1457件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000189 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ONE/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $115.00

## 6. Latest Market Context

- 更新: 2026-08-12T17:11:18.476781+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=63451.4
- Funnel: target 972 → liquid 178 → pre 50 → checked 50 → surge 2 → strict 2
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| COTI/USDT:USDT | +19.78% | $1,107,311.48 |
| JIMOTHY/USDT:USDT | +10.03% | $3,226,044.46 |
| BTW/USDT:USDT | +8.77% | $15,250,500.21 |
| TUT/USDT:USDT | +3.69% | $8,991,045.05 |
| GRVT/USDT:USDT | +3.47% | $1,026,999.94 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SMRSTOCK/USDT:USDT | below_1h_threshold | +2.94% | +2.95% |
| ZEC/USDT:USDT | below_1h_threshold | +2.29% | +2.31% |
| APR/USDT:USDT | below_1h_threshold | +2.25% | +2.27% |
| SPCXSTOCK/USDT:USDT | below_1h_threshold | +1.91% | +1.93% |
| TUT/USDT:USDT | below_1h_threshold | +1.90% | +1.92% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
