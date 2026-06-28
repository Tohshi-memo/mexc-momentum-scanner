# Decision Report

- generated_at: 2026-06-28T00:43:13.277448+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7721**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7721, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-0.27%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.27% | **-0.27%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618 | 4/20 | 20.0% | +5.46% | **+1.09%** |
| LIMIT_BB3S | 4/13 | 30.8% | +0.12% | **+0.04%** |
| LIMIT_10PCT | 3/20 | 15.0% | -0.85% | **-0.13%** |
| LIMIT_9PCT | 3/20 | 15.0% | -1.14% | **-0.17%** |
| ASK | 20/20 | 100.0% | -0.22% | **-0.22%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.27% | **+1.27%** |
| ASK_LONG | 20/20 | 100.0% | +1.19% | **+1.19%** |
| LIMIT_BB3S_LONG | 2/7 | 28.6% | +0.35% | **+0.10%** |
| LIMIT_1PCT_LONG | 13/20 | 65.0% | +0.13% | **+0.09%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | -0.89% | **-0.09%** |

## 2. $100 Live Portfolio

- 残高: **$102.65** / 初期 $100.00 (+2.65%)
- 確定トレード: 41件 (TP 15 / SL 25 / EXP 1)
- 最新: M/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.65
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$238.34** / 初期 $100.00 (+138.34%)
- 確定: 2230件 (Win 670 / Loss 745 / Flat 815) / skip 2052件
- 成長率目線: 平均log +0.000389 / 幾何平均 +0.039% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: VELVET/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $238.34

## 4. Robust Adaptive DryRun ($100)

- 残高: **$107.20** / 初期 $100.00 (+7.20%)
- 確定: 452件 (Win 120 / Loss 117 / Flat 215) / skip 680件
- 成長率目線: 平均log +0.000154 / 幾何平均 +0.015% per trade / maxDD +3.03%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0122 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: VELVET/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $107.20

## 5. Latest Market Context

- 更新: 2026-06-28T00:43:06.178475+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.19% price=60116.7
- Funnel: target 806 → liquid 119 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BAS/USDT:USDT | +17.58% | $2,498,604.18 |
| LAB/USDT:USDT | +14.18% | $42,590,604.14 |
| SLX/USDT:USDT | +12.25% | $19,070,501.94 |
| BASED/USDT:USDT | +8.90% | $1,253,998.52 |
| S/USDT:USDT | +8.61% | $4,532,937.80 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BAS/USDT:USDT | below_1h_threshold | +4.08% | +3.88% |
| BEAT/USDT:USDT | below_1h_threshold | +4.04% | +3.85% |
| LAB/USDT:USDT | below_1h_threshold | +3.89% | +3.69% |
| PIPPIN/USDT:USDT | below_1h_threshold | +3.43% | +3.24% |
| PIEVERSE/USDT:USDT | below_1h_threshold | +3.36% | +3.17% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
