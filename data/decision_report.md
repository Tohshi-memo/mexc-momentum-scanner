# Decision Report

- generated_at: 2026-09-02T02:21:22.045958+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13286**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13286, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.58%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.58% | **-1.58%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 7/20 | 35.0% | +4.44% | **+1.56%** |
| LIMIT_9PCT | 4/20 | 20.0% | +3.29% | **+0.66%** |
| LIMIT_10PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_7PCT | 7/20 | 35.0% | +1.60% | **+0.56%** |
| LIMIT_6PCT | 10/20 | 50.0% | +0.73% | **+0.37%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/3 | 100.0% | +2.87% | **+2.87%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +4.64% | **+2.55%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +4.09% | **+1.84%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +1.94% | **+1.65%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +1.72% | **+1.63%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 196件 (TP 73 / SL 118 / EXP 5)
- 最新: BTR/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$840.39** / 初期 $100.00 (+740.39%)
- 確定: 4921件 (Win 1500 / Loss 1619 / Flat 1802) / skip 4926件
- 成長率目線: 平均log +0.000433 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HEMI/USDT:USDT `LIMIT_1PCT_LONG` TP_HIT account +1.00% 残高後 $840.39

## 4. Robust Adaptive DryRun ($100)

- 残高: **$174.61** / 初期 $100.00 (+74.61%)
- 確定: 2265件 (Win 634 / Loss 545 / Flat 1086) / skip 4432件
- 成長率目線: 平均log +0.000246 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1259 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: HEMI/USDT:USDT `LIMIT_7PCT` SL_HIT account -0.35% 残高後 $174.61

## 5. Causal Adaptive DryRun ($100)

- 残高: **$114.88** / 初期 $100.00 (+14.88%)
- 確定: 2089件 (Win 610 / Loss 817 / Flat 662) / pending 0件 / skip 2668件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000304 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: FILECOIN/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $114.88

## 6. Latest Market Context

- 更新: 2026-09-02T02:21:10.627233+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.20% price=77136.3
- Funnel: target 1036 → liquid 159 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 72.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| UAI/USDT:USDT | +28.29% | $17,649,390.57 |
| MAGMA/USDT:USDT | +27.01% | $4,912,218.78 |
| HEMI/USDT:USDT | +22.25% | $5,520,298.67 |
| FONE/USDT:USDT | +10.24% | $1,378,931.88 |
| BEAT/USDT:USDT | +9.35% | $6,991,279.71 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CASHCAT/USDT:USDT | below_1h_threshold | +2.61% | +2.42% |
| SKYAI/USDT:USDT | below_1h_threshold | +2.31% | +2.11% |
| BTW/USDT:USDT | below_1h_threshold | +2.20% | +2.01% |
| DOS/USDT:USDT | below_1h_threshold | +1.84% | +1.64% |
| AKE/USDT:USDT | below_1h_threshold | +1.81% | +1.61% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
