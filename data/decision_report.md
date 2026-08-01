# Decision Report

- generated_at: 2026-08-01T03:01:16.659068+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10052**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.73% / filled 20/20。**
- 全期間 MARKET基準: n=10052, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.73%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.73% | **+1.73%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.73% | **+1.73%** |
| LIMIT_1PCT | 16/20 | 80.0% | +1.54% | **+1.23%** |
| LIMIT_7PCT | 5/20 | 25.0% | +1.12% | **+0.28%** |
| LIMIT_FIB1618 | 3/20 | 15.0% | +1.63% | **+0.25%** |
| LIMIT_9PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |
| LIMIT_FIB1272_LONG | 12/20 | 60.0% | +0.45% | **+0.27%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | -0.60% | **-0.09%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | -0.29% | **-0.12%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | -0.28% | **-0.13%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$563.34** / 初期 $100.00 (+463.34%)
- 確定: 3604件 (Win 1150 / Loss 1180 / Flat 1274) / skip 3009件
- 成長率目線: 平均log +0.000480 / 幾何平均 +0.048% per trade / maxDD +8.13%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: KOMA/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $563.34

## 4. Robust Adaptive DryRun ($100)

- 残高: **$140.81** / 初期 $100.00 (+40.81%)
- 確定: 1279件 (Win 359 / Loss 297 / Flat 623) / skip 2184件
- 成長率目線: 平均log +0.000268 / 幾何平均 +0.027% per trade / maxDD +3.89%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0250 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: KOMA/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $140.81

## 5. Causal Adaptive DryRun ($100)

- 残高: **$111.99** / 初期 $100.00 (+11.99%)
- 確定: 871件 (Win 282 / Loss 344 / Flat 245) / pending 5件 / skip 651件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000212 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: KOMA/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $111.99

## 6. Latest Market Context

- 更新: 2026-08-01T03:01:08.509521+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=63045.7
- Funnel: target 921 → liquid 167 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| JIMOTHY/USDT:USDT | +39.78% | $1,148,607.86 |
| KOMA/USDT:USDT | +25.21% | $17,846,038.98 |
| TLM/USDT:USDT | +16.98% | $1,837,004.58 |
| BTW/USDT:USDT | +14.99% | $2,460,172.35 |
| GIGGLE/USDT:USDT | +11.88% | $23,351,600.65 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| US/USDT:USDT | below_1h_threshold | +1.58% | +1.57% |
| LAB/USDT:USDT | below_1h_threshold | +0.71% | +0.70% |
| DIA/USDT:USDT | below_1h_threshold | +0.60% | +0.60% |
| KOMA/USDT:USDT | below_1h_threshold | +0.58% | +0.57% |
| BEAT/USDT:USDT | below_1h_threshold | +0.58% | +0.57% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
