# Decision Report

- generated_at: 2026-08-26T05:56:33.210725+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12672**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=12672, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-2.18%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.18% | **-2.18%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 8/20 | 40.0% | +2.20% | **+0.88%** |
| LIMIT_9PCT | 4/20 | 20.0% | +2.00% | **+0.40%** |
| LIMIT_10PCT | 4/20 | 20.0% | +2.00% | **+0.40%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +0.90% | **+0.31%** |
| LIMIT_8PCT | 5/20 | 25.0% | -0.06% | **-0.01%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +2.58% | **+2.58%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +3.12% | **+2.50%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +3.60% | **+2.34%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +2.69% | **+1.61%** |
| LIMIT_3PCT_LONG | 7/20 | 35.0% | +2.63% | **+0.92%** |

## 2. $100 Live Portfolio

- 残高: **$121.16** / 初期 $100.00 (+21.16%)
- 確定トレード: 192件 (TP 73 / SL 114 / EXP 5)
- 最新: CATE/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.16
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$687.36** / 初期 $100.00 (+587.36%)
- 確定: 4585件 (Win 1392 / Loss 1506 / Flat 1687) / skip 4648件
- 成長率目線: 平均log +0.000420 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PONS/USDT:USDT `LIMIT_4PCT_LONG` EXPIRED account +0.00% 残高後 $687.36

## 4. Robust Adaptive DryRun ($100)

- 残高: **$155.51** / 初期 $100.00 (+55.51%)
- 確定: 1978件 (Win 536 / Loss 473 / Flat 969) / skip 4105件
- 成長率目線: 平均log +0.000223 / 幾何平均 +0.022% per trade / maxDD +3.96%
- 次の候補: `LIMIT_7PCT` (selected_by_robust_growth_score) / robust_score +0.0814 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BMT/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $155.51

## 5. Causal Adaptive DryRun ($100)

- 残高: **$114.83** / 初期 $100.00 (+14.83%)
- 確定: 1949件 (Win 569 / Loss 744 / Flat 636) / pending 4件 / skip 2191件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000292 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BTR/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $114.83

## 6. Latest Market Context

- 更新: 2026-08-26T05:56:22.045624+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.21% price=78960.5
- Funnel: target 1023 → liquid 170 → pre 50 → checked 50 → surge 3 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 89.0 >= 65=1, 4h RSI 74.2 >= 65=1, 4h RSI 69.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BTR/USDT:USDT | +105.27% | $3,266,515.77 |
| PORTAL/USDT:USDT | +45.90% | $1,859,482.93 |
| BMT/USDT:USDT | +35.91% | $11,103,065.01 |
| PONS/USDT:USDT | +29.27% | $1,182,793.71 |
| LONGXIA/USDT:USDT | +25.82% | $1,883,719.40 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BICO/USDT:USDT | below_1h_threshold | +4.03% | +3.82% |
| BR/USDT:USDT | below_1h_threshold | +2.88% | +2.67% |
| PONS/USDT:USDT | below_1h_threshold | +2.88% | +2.66% |
| USELESS/USDT:USDT | below_1h_threshold | +2.85% | +2.63% |
| LONGXIA/USDT:USDT | below_1h_threshold | +2.23% | +2.02% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
