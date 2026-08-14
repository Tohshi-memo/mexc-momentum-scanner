# Decision Report

- generated_at: 2026-08-14T10:21:31.244843+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11530**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=11530, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-1.60%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.60% | **-1.60%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618 | 2/20 | 10.0% | +3.88% | **+0.39%** |
| LIMIT_BB3S | 6/16 | 37.5% | +0.72% | **+0.27%** |
| LIMIT_8PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_5PCT | 8/20 | 40.0% | +0.33% | **+0.13%** |
| LIMIT_6PCT | 4/20 | 20.0% | +0.42% | **+0.08%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.20% | **+1.20%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +1.69% | **+1.01%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +1.22% | **+0.92%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +0.80% | **+0.40%** |
| LIMIT_4PCT_LONG | 8/20 | 40.0% | +0.50% | **+0.20%** |

## 2. $100 Live Portfolio

- 残高: **$121.65** / 初期 $100.00 (+21.65%)
- 確定トレード: 182件 (TP 71 / SL 106 / EXP 5)
- 最新: GUA/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.65
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$616.31** / 初期 $100.00 (+516.31%)
- 確定: 3998件 (Win 1249 / Loss 1311 / Flat 1438) / skip 4093件
- 成長率目線: 平均log +0.000455 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AKE/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $616.31

## 4. Robust Adaptive DryRun ($100)

- 残高: **$149.41** / 初期 $100.00 (+49.41%)
- 確定: 1651件 (Win 471 / Loss 398 / Flat 782) / skip 3290件
- 成長率目線: 平均log +0.000243 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0753 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: VELVET/USDT:USDT `LIMIT_5PCT` SL_HIT account -0.35% 残高後 $149.41

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.20** / 初期 $100.00 (+17.20%)
- 確定: 1491件 (Win 445 / Loss 565 / Flat 481) / pending 3件 / skip 1506件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000263 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: AKE/USDT:USDT `MARKET_LONG` EXPIRED account +0.17% 残高後 $117.20

## 6. Latest Market Context

- 更新: 2026-08-14T10:21:17.128938+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.16% price=62860.0
- Funnel: target 981 → liquid 179 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 80.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ACE/USDT:USDT | +66.38% | $14,567,619.27 |
| AKE/USDT:USDT | +48.99% | $66,868,577.64 |
| VELVET/USDT:USDT | +33.03% | $30,310,582.57 |
| 2Z/USDT:USDT | +23.30% | $1,591,663.85 |
| CAP/USDT:USDT | +19.79% | $4,196,858.54 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ACE/USDT:USDT | below_1h_threshold | +4.94% | +4.79% |
| 2Z/USDT:USDT | below_1h_threshold | +4.74% | +4.58% |
| SNXX/USDT:USDT | below_1h_threshold | +3.36% | +3.20% |
| AVAAI/USDT:USDT | below_1h_threshold | +3.10% | +2.94% |
| CAP/USDT:USDT | below_1h_threshold | +2.24% | +2.08% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
