# Decision Report

- generated_at: 2026-07-16T02:01:14.827107+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8780**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.42% / filled 20/20。**
- 全期間 MARKET基準: n=8780, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+2.42%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.42% | **+2.42%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.42% | **+2.42%** |
| LIMIT_1PCT | 19/20 | 95.0% | +2.44% | **+2.31%** |
| LIMIT_2PCT | 17/20 | 85.0% | +2.25% | **+1.91%** |
| LIMIT_ATR | 12/20 | 60.0% | +2.21% | **+1.33%** |
| LIMIT_3PCT | 12/20 | 60.0% | +1.37% | **+0.82%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 11/20 | 55.0% | +1.09% | **+0.60%** |
| LIMIT_10PCT_LONG | 6/20 | 30.0% | +1.04% | **+0.31%** |
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +0.85% | **+0.25%** |
| LIMIT_BB3S_LONG | 10/10 | 100.0% | -0.33% | **-0.33%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | -1.88% | **-0.38%** |

## 2. $100 Live Portfolio

- 残高: **$104.25** / 初期 $100.00 (+4.25%)
- 確定トレード: 100件 (TP 35 / SL 63 / EXP 2)
- 最新: ROAM/USDT:USDT TP_HIT PnL +8.00% 残高後 $104.25
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$340.65** / 初期 $100.00 (+240.65%)
- 確定: 2896件 (Win 906 / Loss 942 / Flat 1048) / skip 2445件
- 成長率目線: 平均log +0.000423 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `LIMIT_7PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ROAM/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $340.65

## 4. Robust Adaptive DryRun ($100)

- 残高: **$107.10** / 初期 $100.00 (+7.10%)
- 確定: 744件 (Win 170 / Loss 168 / Flat 406) / skip 1447件
- 成長率目線: 平均log +0.000092 / 幾何平均 +0.009% per trade / maxDD +3.89%
- 次の候補: `LIMIT_7PCT` (selected_by_robust_growth_score) / robust_score +0.0938 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ALCH/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $107.10

## 5. Causal Adaptive DryRun ($100)

- 残高: **$98.49** / 初期 $100.00 (-1.51%)
- 確定: 64件 (Win 19 / Loss 41 / Flat 4) / pending 0件 / skip 184件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000524 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: XEC/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account -0.09% 残高後 $98.49

## 6. Latest Market Context

- 更新: 2026-07-16T02:01:09.581834+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=64704.9
- Funnel: target 873 → liquid 168 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CAP/USDT:USDT | +17.84% | $1,793,752.17 |
| HOME/USDT:USDT | +15.60% | $2,009,389.56 |
| ROAM/USDT:USDT | +12.14% | $5,659,868.34 |
| ONDO/USDT:USDT | +10.14% | $49,639,952.31 |
| SKL/USDT:USDT | +10.04% | $1,871,363.57 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SNXX/USDT:USDT | below_1h_threshold | +1.28% | +1.27% |
| ALABSTOCK/USDT:USDT | below_1h_threshold | +0.68% | +0.67% |
| SNDKSTOCK/USDT:USDT | below_1h_threshold | +0.60% | +0.59% |
| NBISSTOCK/USDT:USDT | below_1h_threshold | +0.60% | +0.59% |
| AMDSTOCK/USDT:USDT | below_1h_threshold | +0.55% | +0.54% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
