# Decision Report

- generated_at: 2026-08-18T13:01:29.184908+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11904**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.33% / filled 20/20。**
- 全期間 MARKET基準: n=11904, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+1.33%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.33% | **+1.33%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.33% | **+1.33%** |
| LIMIT_1PCT | 17/20 | 85.0% | +0.72% | **+0.61%** |
| LIMIT_4PCT | 11/20 | 55.0% | +1.09% | **+0.60%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +1.53% | **+0.54%** |
| LIMIT_BB3S | 3/20 | 15.0% | +3.50% | **+0.52%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +6.27% | **+1.25%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +3.00% | **+1.20%** |
| LIMIT_1PCT_LONG | 20/20 | 100.0% | +0.82% | **+0.82%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +1.26% | **+0.76%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +1.12% | **+0.50%** |

## 2. $100 Live Portfolio

- 残高: **$121.41** / 初期 $100.00 (+21.41%)
- 確定トレード: 187件 (TP 72 / SL 110 / EXP 5)
- 最新: HEMI/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.41
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$616.52** / 初期 $100.00 (+516.52%)
- 確定: 4204件 (Win 1295 / Loss 1373 / Flat 1536) / skip 4261件
- 成長率目線: 平均log +0.000433 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ACE/USDT:USDT `LIMIT_7PCT_LONG` EXPIRED account +0.00% 残高後 $616.52

## 4. Robust Adaptive DryRun ($100)

- 残高: **$155.25** / 初期 $100.00 (+55.25%)
- 確定: 1820件 (Win 502 / Loss 427 / Flat 891) / skip 3495件
- 成長率目線: 平均log +0.000242 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `LIMIT_FIB1272` (selected_by_robust_growth_score) / robust_score -0.0033 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ACE/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $155.25

## 5. Causal Adaptive DryRun ($100)

- 残高: **$118.84** / 初期 $100.00 (+18.84%)
- 確定: 1715件 (Win 513 / Loss 651 / Flat 551) / pending 6件 / skip 1658件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000482 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ACE/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $118.84

## 6. Latest Market Context

- 更新: 2026-08-18T13:01:20.759699+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.07% price=64152.1
- Funnel: target 993 → liquid 177 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ACE/USDT:USDT | +22.87% | $33,066,509.67 |
| PRL/USDT:USDT | +19.74% | $3,735,095.76 |
| VVV/USDT:USDT | +15.65% | $8,157,936.73 |
| GPS/USDT:USDT | +15.38% | $28,953,358.96 |
| OPN/USDT:USDT | +15.15% | $2,775,974.93 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ACE/USDT:USDT | below_1h_threshold | +0.88% | +0.94% |
| BTW/USDT:USDT | below_1h_threshold | +0.68% | +0.75% |
| SOXS/USDT:USDT | below_1h_threshold | +0.54% | +0.61% |
| VVV/USDT:USDT | below_1h_threshold | +0.32% | +0.39% |
| LAB/USDT:USDT | below_1h_threshold | +0.32% | +0.39% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
