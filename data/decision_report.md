# Decision Report

- generated_at: 2026-08-18T00:21:20.911947+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11862**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.27% / filled 20/20。**
- 全期間 MARKET基準: n=11862, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.27%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.27% | **+1.27%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.27% | **+1.27%** |
| LIMIT_2PCT | 14/20 | 70.0% | +1.27% | **+0.89%** |
| LIMIT_1PCT | 16/20 | 80.0% | +0.62% | **+0.49%** |
| LIMIT_5PCT | 6/20 | 30.0% | +1.30% | **+0.39%** |
| LIMIT_ATR | 14/20 | 70.0% | +0.52% | **+0.37%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +2.82% | **+0.56%** |
| LIMIT_FIB1272_LONG | 12/20 | 60.0% | +0.89% | **+0.53%** |
| LIMIT_5PCT_LONG | 12/20 | 60.0% | +0.66% | **+0.39%** |
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +0.35% | **+0.22%** |
| LIMIT_BB3S_LONG | 7/9 | 77.8% | +0.19% | **+0.15%** |

## 2. $100 Live Portfolio

- 残高: **$121.41** / 初期 $100.00 (+21.41%)
- 確定トレード: 187件 (TP 72 / SL 110 / EXP 5)
- 最新: HEMI/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.41
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$611.63** / 初期 $100.00 (+511.63%)
- 確定: 4187件 (Win 1292 / Loss 1366 / Flat 1529) / skip 4236件
- 成長率目線: 平均log +0.000433 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: NIULAI/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $611.63

## 4. Robust Adaptive DryRun ($100)

- 残高: **$155.25** / 初期 $100.00 (+55.25%)
- 確定: 1819件 (Win 502 / Loss 427 / Flat 890) / skip 3454件
- 成長率目線: 平均log +0.000242 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0669 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: NIULAI/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $155.25

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.53** / 初期 $100.00 (+17.53%)
- 確定: 1679件 (Win 504 / Loss 641 / Flat 534) / pending 0件 / skip 1655件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000176 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: AIO/USDT:USDT `MARKET` TP_HIT account +0.34% 残高後 $117.53

## 6. Latest Market Context

- 更新: 2026-08-18T00:21:12.556218+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.13% price=64417.6
- Funnel: target 992 → liquid 176 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PIEVERSE/USDT:USDT | +11.67% | $1,098,384.38 |
| COMP/USDT:USDT | +7.15% | $2,993,328.57 |
| ACU/USDT:USDT | +7.14% | $1,236,445.50 |
| ANSEM/USDT:USDT | +7.10% | $3,830,754.05 |
| TUT/USDT:USDT | +6.41% | $27,952,190.21 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| US/USDT:USDT | below_1h_threshold | +2.57% | +2.71% |
| TUT/USDT:USDT | below_1h_threshold | +2.14% | +2.27% |
| ACU/USDT:USDT | below_1h_threshold | +1.62% | +1.76% |
| DIA/USDT:USDT | below_1h_threshold | +1.34% | +1.48% |
| COMP/USDT:USDT | below_1h_threshold | +0.68% | +0.81% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
