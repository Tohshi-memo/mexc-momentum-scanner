# Decision Report

- generated_at: 2026-08-18T12:36:40.959863+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11903**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.93% / filled 20/20。**
- 全期間 MARKET基準: n=11903, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+1.93%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.93% | **+1.93%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.93% | **+1.93%** |
| LIMIT_1PCT | 16/20 | 80.0% | +1.01% | **+0.81%** |
| LIMIT_4PCT | 10/20 | 50.0% | +1.60% | **+0.80%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +1.22% | **+0.36%** |
| LIMIT_BB3S | 2/20 | 10.0% | +3.22% | **+0.32%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +5.24% | **+1.31%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +2.67% | **+1.20%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +1.10% | **+0.71%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +0.90% | **+0.45%** |
| LIMIT_1PCT_LONG | 20/20 | 100.0% | +0.22% | **+0.22%** |

## 2. $100 Live Portfolio

- 残高: **$121.41** / 初期 $100.00 (+21.41%)
- 確定トレード: 187件 (TP 72 / SL 110 / EXP 5)
- 最新: HEMI/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.41
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$616.52** / 初期 $100.00 (+516.52%)
- 確定: 4203件 (Win 1295 / Loss 1373 / Flat 1535) / skip 4261件
- 成長率目線: 平均log +0.000433 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BASECAT/USDT:USDT `LIMIT_7PCT_LONG` EXPIRED account -0.13% 残高後 $616.52

## 4. Robust Adaptive DryRun ($100)

- 残高: **$155.25** / 初期 $100.00 (+55.25%)
- 確定: 1820件 (Win 502 / Loss 427 / Flat 891) / skip 3494件
- 成長率目線: 平均log +0.000242 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `LIMIT_FIB1272` (selected_by_robust_growth_score) / robust_score -0.0044 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ACE/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $155.25

## 5. Causal Adaptive DryRun ($100)

- 残高: **$119.05** / 初期 $100.00 (+19.05%)
- 確定: 1714件 (Win 513 / Loss 650 / Flat 551) / pending 6件 / skip 1657件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000490 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BASECAT/USDT:USDT `MARKET` TP_HIT account +0.34% 残高後 $119.05

## 6. Latest Market Context

- 更新: 2026-08-18T12:36:25.314738+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.09% price=64266.7
- Funnel: target 993 → liquid 181 → pre 50 → checked 50 → surge 2 → strict 2
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PRL/USDT:USDT | +20.63% | $3,669,964.14 |
| ACE/USDT:USDT | +17.01% | $33,677,431.20 |
| VVV/USDT:USDT | +16.43% | $7,996,381.98 |
| GPS/USDT:USDT | +15.74% | $31,586,349.50 |
| SOXS/USDT:USDT | +14.75% | $9,740,032.59 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| APR/USDT:USDT | below_1h_threshold | +3.25% | +3.34% |
| ANSEM/USDT:USDT | below_1h_threshold | +2.31% | +2.40% |
| BTW/USDT:USDT | below_1h_threshold | +1.43% | +1.53% |
| GUN/USDT:USDT | below_1h_threshold | +1.38% | +1.47% |
| LIT/USDT:USDT | below_1h_threshold | +1.01% | +1.10% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
