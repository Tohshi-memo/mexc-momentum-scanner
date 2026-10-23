# Decision Report

- generated_at: 2026-10-23T23:51:33.424518+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17296**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=17296, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.60%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.60% | **-1.60%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 12/20 | 60.0% | +1.96% | **+1.18%** |
| LIMIT_8PCT | 9/20 | 45.0% | +2.19% | **+0.99%** |
| LIMIT_7PCT | 10/20 | 50.0% | +1.64% | **+0.82%** |
| LIMIT_10PCT | 5/20 | 25.0% | +3.20% | **+0.80%** |
| LIMIT_5PCT | 14/20 | 70.0% | +0.84% | **+0.59%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 15/20 | 75.0% | +0.80% | **+0.60%** |
| LIMIT_5PCT_LONG | 14/20 | 70.0% | +0.29% | **+0.20%** |
| LIMIT_3PCT_LONG | 15/20 | 75.0% | -0.00% | **-0.00%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | -1.00% | **-0.40%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | -0.73% | **-0.40%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 250件 (TP 92 / SL 150 / EXP 8)
- 最新: MSTRSTOCK/USDT:USDT EXPIRED PnL +0.27% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,310.72** / 初期 $100.00 (+1210.72%)
- 確定: 6553件 (Win 1902 / Loss 2094 / Flat 2557) / skip 7304件
- 成長率目線: 平均log +0.000393 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_9PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: UNITREE/USDT:USDT `MARKET` SL_HIT account -0.50% 残高後 $1,310.72

## 4. Robust Adaptive DryRun ($100)

- 残高: **$298.55** / 初期 $100.00 (+198.55%)
- 確定: 3929件 (Win 1083 / Loss 920 / Flat 1926) / skip 6778件
- 成長率目線: 平均log +0.000278 / 幾何平均 +0.028% per trade / maxDD +4.13%
- 次の候補: `LIMIT_8PCT` (selected_by_robust_growth_score) / robust_score +0.1054 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: IRYS/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $298.55

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5456件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_8PCT` (selected_by_causal_log_growth) / causal_score +0.000368 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-23T23:51:18.598825+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.43% price=81136.6
- Funnel: target 1088 → liquid 167 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 70.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AXIS/USDT:USDT | +23.07% | $1,197,412.92 |
| AGT/USDT:USDT | +21.93% | $10,534,220.18 |
| IRYS/USDT:USDT | +20.87% | $94,791,238.04 |
| AKE/USDT:USDT | +10.77% | $18,805,934.97 |
| SOXS/USDT:USDT | +3.93% | $32,137,974.44 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ZKSYNC/USDT:USDT | below_1h_threshold | +3.03% | +2.59% |
| SOXS/USDT:USDT | below_1h_threshold | +1.40% | +0.96% |
| AVAX/USDT:USDT | below_1h_threshold | +1.32% | +0.89% |
| WLFI/USDT:USDT | below_1h_threshold | +1.26% | +0.83% |
| BTW/USDT:USDT | below_1h_threshold | +0.91% | +0.48% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
