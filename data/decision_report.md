# Decision Report

- generated_at: 2026-08-30T00:06:20.699407+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12974**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=12974, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.80%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.80% | **-0.80%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 4/20 | 20.0% | +4.15% | **+0.83%** |
| LIMIT_8PCT | 4/20 | 20.0% | +2.85% | **+0.57%** |
| LIMIT_10PCT | 3/20 | 15.0% | +3.15% | **+0.47%** |
| LIMIT_7PCT | 8/20 | 40.0% | +0.90% | **+0.36%** |
| LIMIT_FIB1272 | 11/20 | 55.0% | +0.62% | **+0.34%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +2.94% | **+2.65%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +3.34% | **+2.50%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +3.29% | **+2.30%** |
| MARKET_LONG | 20/20 | 100.0% | +1.01% | **+1.01%** |
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +0.88% | **+0.39%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 194件 (TP 73 / SL 116 / EXP 5)
- 最新: SKR/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$760.98** / 初期 $100.00 (+660.98%)
- 確定: 4744件 (Win 1443 / Loss 1558 / Flat 1743) / skip 4791件
- 成長率目線: 平均log +0.000428 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PONS/USDT:USDT `LIMIT_1PCT_LONG` TP_HIT account +1.00% 残高後 $760.98

## 4. Robust Adaptive DryRun ($100)

- 残高: **$168.75** / 初期 $100.00 (+68.75%)
- 確定: 2058件 (Win 570 / Loss 494 / Flat 994) / skip 4327件
- 成長率目線: 平均log +0.000254 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1686 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: PONS/USDT:USDT `LIMIT_1PCT_LONG` TP_HIT account +0.69% 残高後 $168.75

## 5. Causal Adaptive DryRun ($100)

- 残高: **$115.05** / 初期 $100.00 (+15.05%)
- 確定: 2037件 (Win 597 / Loss 794 / Flat 646) / pending 0件 / skip 2410件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000417 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: VELVET/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $115.05

## 6. Latest Market Context

- 更新: 2026-08-30T00:06:11.429873+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.04% price=78169.8
- Funnel: target 1023 → liquid 116 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PROM/USDT:USDT | +25.26% | $9,658,739.47 |
| HNT/USDT:USDT | +22.10% | $23,161,421.36 |
| PONS/USDT:USDT | +21.42% | $1,142,689.47 |
| FONE/USDT:USDT | +17.80% | $1,193,506.55 |
| BTR/USDT:USDT | +16.45% | $9,731,582.68 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| FONE/USDT:USDT | below_1h_threshold | +3.24% | +3.28% |
| DOS/USDT:USDT | below_1h_threshold | +2.23% | +2.27% |
| 4/USDT:USDT | below_1h_threshold | +2.12% | +2.16% |
| PONS/USDT:USDT | below_1h_threshold | +1.36% | +1.40% |
| HNT/USDT:USDT | below_1h_threshold | +1.02% | +1.06% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
