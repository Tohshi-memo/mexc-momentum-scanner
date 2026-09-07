# Decision Report

- generated_at: 2026-09-07T20:56:24.907710+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13907**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13907, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.59%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.59% | **-1.59%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 2/20 | 10.0% | +6.29% | **+0.63%** |
| LIMIT_BB3S | 3/20 | 15.0% | +1.74% | **+0.26%** |
| LIMIT_ATR | 8/20 | 40.0% | +0.52% | **+0.21%** |
| LIMIT_8PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +2.20% | **+1.87%** |
| MARKET_LONG | 20/20 | 100.0% | +1.39% | **+1.39%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +2.22% | **+1.33%** |
| LIMIT_3PCT_LONG | 9/20 | 45.0% | +2.58% | **+1.16%** |
| LIMIT_8PCT_LONG | 4/20 | 20.0% | +4.00% | **+0.80%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 206件 (TP 77 / SL 124 / EXP 5)
- 最新: BONER/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$894.98** / 初期 $100.00 (+794.98%)
- 確定: 5180件 (Win 1550 / Loss 1684 / Flat 1946) / skip 5288件
- 成長率目線: 平均log +0.000423 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AKE/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $894.98

## 4. Robust Adaptive DryRun ($100)

- 残高: **$188.18** / 初期 $100.00 (+88.18%)
- 確定: 2572件 (Win 717 / Loss 618 / Flat 1237) / skip 4746件
- 成長率目線: 平均log +0.000246 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ACE/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $188.18

## 5. Causal Adaptive DryRun ($100)

- 残高: **$120.53** / 初期 $100.00 (+20.53%)
- 確定: 2498件 (Win 735 / Loss 939 / Flat 824) / pending 6件 / skip 2876件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000227 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: AKE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $120.53

## 6. Latest Market Context

- 更新: 2026-09-07T20:56:12.493235+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.15% price=79212.0
- Funnel: target 1062 → liquid 147 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SOPH/USDT:USDT | +14.13% | $1,524,171.19 |
| IOST/USDT:USDT | +13.48% | $3,003,914.97 |
| MEMEROBINHOOD/USDT:USDT | +9.94% | $5,549,475.91 |
| AKE/USDT:USDT | +9.14% | $12,505,248.85 |
| AERO/USDT:USDT | +9.13% | $2,916,677.19 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SOPH/USDT:USDT | below_1h_threshold | +4.40% | +4.56% |
| ACE/USDT:USDT | below_1h_threshold | +4.39% | +4.54% |
| ICP/USDT:USDT | below_1h_threshold | +2.11% | +2.27% |
| IOST/USDT:USDT | below_1h_threshold | +2.06% | +2.21% |
| VVV/USDT:USDT | below_1h_threshold | +2.03% | +2.18% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
