# Decision Report

- generated_at: 2026-10-25T09:21:21.263561+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17415**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=17415, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.14%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.14% | **-0.14%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT | 16/20 | 80.0% | +0.83% | **+0.66%** |
| LIMIT_ATR | 14/20 | 70.0% | +0.39% | **+0.27%** |
| LIMIT_10PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_BB3S | 3/16 | 18.8% | +0.76% | **+0.14%** |
| LIMIT_7PCT | 4/20 | 20.0% | +0.70% | **+0.14%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +1.83% | **+1.47%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +1.81% | **+1.18%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +1.58% | **+0.95%** |
| LIMIT_ATR_LONG | 9/20 | 45.0% | +1.94% | **+0.87%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +0.97% | **+0.48%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 250件 (TP 92 / SL 150 / EXP 8)
- 最新: MSTRSTOCK/USDT:USDT EXPIRED PnL +0.27% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,512.52** / 初期 $100.00 (+1412.52%)
- 確定: 6668件 (Win 1938 / Loss 2125 / Flat 2605) / skip 7308件
- 成長率目線: 平均log +0.000407 / 幾何平均 +0.041% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: TAG/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $1,512.52

## 4. Robust Adaptive DryRun ($100)

- 残高: **$310.66** / 初期 $100.00 (+210.66%)
- 確定: 3958件 (Win 1096 / Loss 929 / Flat 1933) / skip 6868件
- 成長率目線: 平均log +0.000286 / 幾何平均 +0.029% per trade / maxDD +4.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1718 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: TAG/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $310.66

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5572件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000560 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-25T09:21:06.513463+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.26% price=80168.8
- Funnel: target 1071 → liquid 128 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| T/USDT:USDT | +42.58% | $5,582,106.32 |
| TAG/USDT:USDT | +30.78% | $1,409,312.63 |
| APR/USDT:USDT | +27.39% | $6,190,013.64 |
| USELESS/USDT:USDT | +15.46% | $4,654,387.09 |
| GRASS/USDT:USDT | +7.79% | $2,085,196.75 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| T/USDT:USDT | below_1h_threshold | +4.60% | +4.85% |
| Q/USDT:USDT | below_1h_threshold | +0.69% | +0.94% |
| SPX/USDT:USDT | below_1h_threshold | +0.00% | +0.26% |
| LTC/USDT:USDT | below_1h_threshold | -0.05% | +0.20% |
| XMR/USDT:USDT | below_1h_threshold | -0.06% | +0.20% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
