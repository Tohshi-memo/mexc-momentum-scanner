# Decision Report

- generated_at: 2026-11-20T21:26:39.159721+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **19270**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=19270, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.59%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.59% | **-0.59%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 5/20 | 25.0% | +4.56% | **+1.14%** |
| LIMIT_9PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_10PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_8PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | +0.73% | **+0.33%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +2.50% | **+1.25%** |
| LIMIT_7PCT_LONG | 6/20 | 30.0% | +3.46% | **+1.04%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.13% | **+0.85%** |
| LIMIT_8PCT_LONG | 4/20 | 20.0% | +4.00% | **+0.80%** |
| LIMIT_ATR_LONG | 10/20 | 50.0% | +1.53% | **+0.77%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 283件 (TP 103 / SL 172 / EXP 8)
- 最新: INTCSTOCK/USDT:USDT TP_HIT PnL +5.26% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,692.31** / 初期 $100.00 (+1592.31%)
- 確定: 7417件 (Win 2133 / Loss 2391 / Flat 2893) / skip 8414件
- 成長率目線: 平均log +0.000381 / 幾何平均 +0.038% per trade / maxDD +8.46%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: UVXY/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $1,692.31

## 4. Robust Adaptive DryRun ($100)

- 残高: **$439.41** / 初期 $100.00 (+339.41%)
- 確定: 5087件 (Win 1354 / Loss 1088 / Flat 2645) / skip 7594件
- 成長率目線: 平均log +0.000291 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score -0.0054 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: UVXY/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $439.41

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7431件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000101 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-20T21:26:22.470354+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.41% price=58674.9
- Funnel: target 1087 → liquid 162 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 81.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AKE/USDT:USDT | +32.61% | $25,333,256.81 |
| PIEVERSE/USDT:USDT | +14.74% | $4,223,510.98 |
| UVXY/USDT:USDT | +10.44% | $6,812,281.87 |
| BTW/USDT:USDT | +8.59% | $3,920,736.64 |
| SKDD/USDT:USDT | +7.00% | $1,031,634.98 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SOXS/USDT:USDT | below_1h_threshold | +3.25% | +2.84% |
| BTW/USDT:USDT | below_1h_threshold | +3.04% | +2.63% |
| AKE/USDT:USDT | below_1h_threshold | +2.80% | +2.39% |
| SQQQ/USDT:USDT | below_1h_threshold | +2.38% | +1.96% |
| VELVET/USDT:USDT | below_1h_threshold | +2.14% | +1.73% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
