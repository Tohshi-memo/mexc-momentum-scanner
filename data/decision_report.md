# Decision Report

- generated_at: 2026-09-13T09:16:30.591172+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14404**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=14404, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.40% | **-0.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 6/20 | 30.0% | +2.94% | **+0.88%** |
| LIMIT_5PCT | 8/20 | 40.0% | +2.10% | **+0.84%** |
| LIMIT_BB3S | 2/12 | 16.7% | +3.31% | **+0.55%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.27% | **+0.34%** |
| LIMIT_8PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 10/20 | 50.0% | +4.03% | **+2.01%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +2.47% | **+0.99%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.14% | **+0.97%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +1.42% | **+0.92%** |
| MARKET_LONG | 20/20 | 100.0% | +0.60% | **+0.60%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 211件 (TP 78 / SL 128 / EXP 5)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,080.43** / 初期 $100.00 (+980.43%)
- 確定: 5431件 (Win 1635 / Loss 1760 / Flat 2036) / skip 5534件
- 成長率目線: 平均log +0.000438 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: VTHO/USDT:USDT `LIMIT_BB3S_LONG` EXPIRED account +0.00% 残高後 $1,080.43

## 4. Robust Adaptive DryRun ($100)

- 残高: **$225.54** / 初期 $100.00 (+125.54%)
- 確定: 2922件 (Win 813 / Loss 692 / Flat 1417) / skip 4893件
- 成長率目線: 平均log +0.000278 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1416 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: LSK/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $225.54

## 5. Causal Adaptive DryRun ($100)

- 残高: **$127.29** / 初期 $100.00 (+27.29%)
- 確定: 2848件 (Win 848 / Loss 1099 / Flat 901) / pending 6件 / skip 3027件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000378 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: REZ/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $127.29

## 6. Latest Market Context

- 更新: 2026-09-13T09:16:15.439209+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.04% price=76740.1
- Funnel: target 1068 → liquid 130 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 95.8 >= 65=1, 4h RSI 67.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LSK/USDT:USDT | +205.97% | $89,228,043.91 |
| STEEM/USDT:USDT | +64.05% | $1,282,678.05 |
| ARK/USDT:USDT | +40.03% | $1,254,937.04 |
| VTHO/USDT:USDT | +36.01% | $3,136,297.46 |
| POWR/USDT:USDT | +29.80% | $2,479,947.13 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| STORJ/USDT:USDT | below_1h_threshold | +4.31% | +4.35% |
| CRV/USDT:USDT | below_1h_threshold | +4.26% | +4.30% |
| ZCAT/USDT:USDT | below_1h_threshold | +3.74% | +3.78% |
| KOMA/USDT:USDT | below_1h_threshold | +3.20% | +3.24% |
| POWR/USDT:USDT | below_1h_threshold | +2.32% | +2.36% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
