# Decision Report

- generated_at: 2026-10-24T16:31:30.838530+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17381**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=17381, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 10/20 | 50.0% | +2.57% | **+1.28%** |
| LIMIT_7PCT | 8/20 | 40.0% | +2.85% | **+1.14%** |
| LIMIT_5PCT | 12/20 | 60.0% | +1.48% | **+0.89%** |
| LIMIT_FIB1272 | 4/20 | 20.0% | +3.84% | **+0.77%** |
| LIMIT_ATR | 11/20 | 55.0% | +1.25% | **+0.69%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 20/20 | 100.0% | +1.41% | **+1.41%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +1.43% | **+1.21%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +1.14% | **+0.80%** |
| LIMIT_ATR_LONG | 7/20 | 35.0% | +1.24% | **+0.43%** |
| LIMIT_BB3S_LONG | 3/4 | 75.0% | +0.00% | **+0.00%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 250件 (TP 92 / SL 150 / EXP 8)
- 最新: MSTRSTOCK/USDT:USDT EXPIRED PnL +0.27% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,407.56** / 初期 $100.00 (+1307.56%)
- 確定: 6634件 (Win 1922 / Loss 2114 / Flat 2598) / skip 7308件
- 成長率目線: 平均log +0.000399 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ORDER/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +1.00% 残高後 $1,407.56

## 4. Robust Adaptive DryRun ($100)

- 残高: **$298.55** / 初期 $100.00 (+198.55%)
- 確定: 3930件 (Win 1083 / Loss 920 / Flat 1927) / skip 6862件
- 成長率目線: 平均log +0.000278 / 幾何平均 +0.028% per trade / maxDD +4.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1838 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BIRB/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $298.55

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5541件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000583 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-24T16:31:13.788818+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.19% price=79614.5
- Funnel: target 1079 → liquid 141 → pre 50 → checked 50 → surge 2 → strict 2
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AKE/USDT:USDT | +9.49% | $13,338,223.94 |
| DNA/USDT:USDT | +6.20% | $1,683,559.84 |
| ORDER/USDT:USDT | +4.30% | $11,289,830.37 |
| IRYS/USDT:USDT | +3.32% | $87,496,084.27 |
| Q/USDT:USDT | +1.92% | $3,243,892.30 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ORDER/USDT:USDT | below_1h_threshold | +4.17% | +4.36% |
| IRYS/USDT:USDT | below_1h_threshold | +3.34% | +3.53% |
| JCT/USDT:USDT | below_1h_threshold | +2.64% | +2.82% |
| Q/USDT:USDT | below_1h_threshold | +1.93% | +2.11% |
| BMT/USDT:USDT | below_1h_threshold | +1.87% | +2.06% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
