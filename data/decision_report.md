# Decision Report

- generated_at: 2026-11-08T15:41:23.663546+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18464**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=18464, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-1.78%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.78% | **-1.78%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 7/20 | 35.0% | +4.57% | **+1.60%** |
| LIMIT_10PCT | 6/20 | 30.0% | +4.00% | **+1.20%** |
| LIMIT_8PCT | 8/20 | 40.0% | +2.96% | **+1.19%** |
| LIMIT_7PCT | 9/20 | 45.0% | +1.51% | **+0.68%** |
| LIMIT_4PCT | 16/20 | 80.0% | +0.04% | **+0.03%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +3.72% | **+2.42%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +3.22% | **+1.93%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +2.28% | **+1.82%** |
| LIMIT_7PCT_LONG | 6/20 | 30.0% | +4.97% | **+1.49%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +2.12% | **+1.49%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 265件 (TP 97 / SL 160 / EXP 8)
- 最新: JCT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,675.79** / 初期 $100.00 (+1575.79%)
- 確定: 7150件 (Win 2057 / Loss 2279 / Flat 2814) / skip 7875件
- 成長率目線: 平均log +0.000394 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ARIA/USDT:USDT `LIMIT_4PCT_LONG` EXPIRED account +0.04% 残高後 $1,675.79

## 4. Robust Adaptive DryRun ($100)

- 残高: **$389.21** / 初期 $100.00 (+289.21%)
- 確定: 4755件 (Win 1277 / Loss 1047 / Flat 2431) / skip 7120件
- 成長率目線: 平均log +0.000286 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1249 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CLAUDIA/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $389.21

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6624件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000419 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-08T15:41:10.466116+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.06% price=76054.4
- Funnel: target 1089 → liquid 103 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 88.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CLAUDIA/USDT:USDT | +313.10% | $15,021,606.28 |
| JCT/USDT:USDT | +224.85% | $27,373,072.66 |
| AIOT/USDT:USDT | +29.00% | $3,332,802.36 |
| SKYAI/USDT:USDT | +19.51% | $1,182,741.90 |
| HOT/USDT:USDT | +18.49% | $4,289,337.91 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ICNT/USDT:USDT | below_1h_threshold | +3.28% | +3.21% |
| LSK/USDT:USDT | below_1h_threshold | +1.18% | +1.11% |
| DASH/USDT:USDT | below_1h_threshold | +1.16% | +1.09% |
| TRUMPOFFICIAL/USDT:USDT | below_1h_threshold | +0.68% | +0.61% |
| FLOKI/USDT:USDT | below_1h_threshold | +0.66% | +0.60% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
