# Decision Report

- generated_at: 2026-08-08T23:46:37.570582+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10896**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.45% / filled 20/20。**
- 全期間 MARKET基準: n=10896, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.45%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.45% | **+0.45%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +1.09% | **+1.03%** |
| LIMIT_2PCT | 17/20 | 85.0% | +1.07% | **+0.91%** |
| MARKET | 20/20 | 100.0% | +0.45% | **+0.45%** |
| LIMIT_ATR | 14/20 | 70.0% | +0.45% | **+0.31%** |
| LIMIT_3PCT | 15/20 | 75.0% | +0.02% | **+0.01%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +2.06% | **+0.83%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +0.67% | **+0.30%** |
| LIMIT_FIB1272_LONG | 6/20 | 30.0% | -0.04% | **-0.01%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | -0.03% | **-0.01%** |
| MARKET_LONG | 20/20 | 100.0% | -0.08% | **-0.08%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 176件 (TP 67 / SL 104 / EXP 5)
- 最新: AAOISTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$636.22** / 初期 $100.00 (+536.22%)
- 確定: 3897件 (Win 1224 / Loss 1269 / Flat 1404) / skip 3560件
- 成長率目線: 平均log +0.000475 / 幾何平均 +0.047% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: TUT/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $636.22

## 4. Robust Adaptive DryRun ($100)

- 残高: **$142.00** / 初期 $100.00 (+42.00%)
- 確定: 1511件 (Win 424 / Loss 360 / Flat 727) / skip 2796件
- 成長率目線: 平均log +0.000232 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0231 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CAT/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $142.00

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.55** / 初期 $100.00 (+17.55%)
- 確定: 1247件 (Win 390 / Loss 479 / Flat 378) / pending 1件 / skip 1124件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000053 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: FORM/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.03% 残高後 $117.55

## 6. Latest Market Context

- 更新: 2026-08-08T23:46:29.820323+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.04% price=64942.5
- Funnel: target 961 → liquid 152 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TUT/USDT:USDT | +46.96% | $22,059,692.48 |
| COOKIE/USDT:USDT | +28.85% | $2,863,210.20 |
| CYS/USDT:USDT | +14.80% | $31,195,787.21 |
| SAGA/USDT:USDT | +14.70% | $1,225,389.66 |
| BLUAI/USDT:USDT | +13.97% | $7,110,236.69 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BICO/USDT:USDT | below_1h_threshold | +4.83% | +4.79% |
| TUT/USDT:USDT | below_1h_threshold | +4.20% | +4.16% |
| BLUAI/USDT:USDT | below_1h_threshold | +3.97% | +3.93% |
| COOKIE/USDT:USDT | below_1h_threshold | +2.36% | +2.32% |
| CYS/USDT:USDT | below_1h_threshold | +2.16% | +2.11% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
