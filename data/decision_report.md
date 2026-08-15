# Decision Report

- generated_at: 2026-08-15T11:26:21.057611+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11661**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +3.80% / filled 20/20。**
- 全期間 MARKET基準: n=11661, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+3.80%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +3.80% | **+3.80%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +3.80% | **+3.80%** |
| LIMIT_2PCT | 13/20 | 65.0% | +3.40% | **+2.21%** |
| LIMIT_1PCT | 15/20 | 75.0% | +2.74% | **+2.06%** |
| LIMIT_3PCT | 11/20 | 55.0% | +2.29% | **+1.26%** |
| LIMIT_BB3S | 3/15 | 20.0% | +2.30% | **+0.46%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 7/20 | 35.0% | +5.52% | **+1.93%** |
| LIMIT_9PCT_LONG | 8/20 | 40.0% | +3.91% | **+1.56%** |
| LIMIT_8PCT_LONG | 13/20 | 65.0% | +0.62% | **+0.40%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | -0.37% | **-0.07%** |
| LIMIT_FIB1272_LONG | 13/20 | 65.0% | -0.43% | **-0.28%** |

## 2. $100 Live Portfolio

- 残高: **$121.65** / 初期 $100.00 (+21.65%)
- 確定トレード: 182件 (TP 71 / SL 106 / EXP 5)
- 最新: GUA/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.65
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$644.59** / 初期 $100.00 (+544.59%)
- 確定: 4129件 (Win 1290 / Loss 1354 / Flat 1485) / skip 4093件
- 成長率目線: 平均log +0.000451 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `LIMIT_10PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CYS/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $644.59

## 4. Robust Adaptive DryRun ($100)

- 残高: **$155.41** / 初期 $100.00 (+55.41%)
- 確定: 1724件 (Win 489 / Loss 412 / Flat 823) / skip 3348件
- 成長率目線: 平均log +0.000256 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1149 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CYS/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $155.41

## 5. Causal Adaptive DryRun ($100)

- 残高: **$119.32** / 初期 $100.00 (+19.32%)
- 確定: 1603件 (Win 488 / Loss 605 / Flat 510) / pending 4件 / skip 1525件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000523 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CYS/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $119.32

## 6. Latest Market Context

- 更新: 2026-08-15T11:26:14.537023+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=63003.9
- Funnel: target 985 → liquid 154 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| COW/USDT:USDT | +55.50% | $4,242,698.17 |
| ROBO/USDT:USDT | +28.41% | $7,344,449.57 |
| ANSEM/USDT:USDT | +27.57% | $1,560,054.23 |
| VELVET/USDT:USDT | +24.11% | $32,960,149.15 |
| US/USDT:USDT | +20.10% | $6,116,632.84 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AIO/USDT:USDT | below_1h_threshold | +4.84% | +4.85% |
| COW/USDT:USDT | below_1h_threshold | +2.70% | +2.72% |
| TUT/USDT:USDT | below_1h_threshold | +2.60% | +2.62% |
| ONE/USDT:USDT | below_1h_threshold | +2.35% | +2.36% |
| H/USDT:USDT | below_1h_threshold | +2.06% | +2.08% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
