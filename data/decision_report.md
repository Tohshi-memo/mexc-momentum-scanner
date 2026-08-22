# Decision Report

- generated_at: 2026-08-22T04:46:51.687825+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12316**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=12316, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.27%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.27% | **-1.27%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 6/20 | 30.0% | +2.67% | **+0.80%** |
| LIMIT_8PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_2PCT | 19/20 | 95.0% | +0.37% | **+0.35%** |
| LIMIT_3PCT | 17/20 | 85.0% | +0.41% | **+0.35%** |
| LIMIT_5PCT | 8/20 | 40.0% | +0.33% | **+0.13%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 12/20 | 60.0% | +3.52% | **+2.11%** |
| MARKET_LONG | 20/20 | 100.0% | +1.86% | **+1.86%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +2.14% | **+1.71%** |
| LIMIT_6PCT_LONG | 5/20 | 25.0% | +5.60% | **+1.40%** |
| LIMIT_BB3S_LONG | 4/10 | 40.0% | +2.62% | **+1.05%** |

## 2. $100 Live Portfolio

- 残高: **$121.04** / 初期 $100.00 (+21.04%)
- 確定トレード: 190件 (TP 72 / SL 113 / EXP 5)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.04
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$715.87** / 初期 $100.00 (+615.87%)
- 確定: 4434件 (Win 1359 / Loss 1446 / Flat 1629) / skip 4443件
- 成長率目線: 平均log +0.000444 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: NIULAI/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $715.87

## 4. Robust Adaptive DryRun ($100)

- 残高: **$156.05** / 初期 $100.00 (+56.05%)
- 確定: 1922件 (Win 528 / Loss 459 / Flat 935) / skip 3805件
- 成長率目線: 平均log +0.000232 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.2067 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: NIULAI/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $156.05

## 5. Causal Adaptive DryRun ($100)

- 残高: **$118.49** / 初期 $100.00 (+18.49%)
- 確定: 1854件 (Win 549 / Loss 698 / Flat 607) / pending 6件 / skip 1942件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000550 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CRO/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $118.49

## 6. Latest Market Context

- 更新: 2026-08-22T04:46:37.074576+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.27% price=78606.8
- Funnel: target 1018 → liquid 222 → pre 50 → checked 50 → surge 11 → strict 1
- Surge前reject: below_1h_threshold=36, below_relative_strength=3, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 89.6 >= 65=2, 4h RSI 84.8 >= 65=1, 4h RSI 95.4 >= 65=1, 4h RSI 79.8 >= 65=1, 4h RSI 90.8 >= 65=1, 4h RSI 77.4 >= 65=1, 4h RSI 94.8 >= 65=1, 4h RSI 71.0 >= 65=1, 4h RSI 90.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BASECAT/USDT:USDT | +250.30% | $4,454,104.18 |
| CATE/USDT:USDT | +78.54% | $11,623,592.94 |
| TRUMPOFFICIAL/USDT:USDT | +56.86% | $44,780,449.64 |
| MUBARAK/USDT:USDT | +41.72% | $1,520,121.88 |
| DASH/USDT:USDT | +28.49% | $16,941,489.53 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ADA/USDT:USDT | below_relative_strength | +5.08% | +4.81% |
| FLOKI/USDT:USDT | below_relative_strength | +5.04% | +4.77% |
| WLD/USDT:USDT | below_relative_strength | +5.00% | +4.73% |
| DOGE/USDT:USDT | below_1h_threshold | +4.74% | +4.47% |
| WIF/USDT:USDT | below_1h_threshold | +4.55% | +4.28% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
